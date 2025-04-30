from flask import render_template, redirect, url_for, flash, request, jsonify, abort
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User, Metric, Alert, Dashboard
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

# Main routes
def index():
    """Landing page view."""
    metrics = Metric.query.all()
    return render_template('auth/index.html', metrics=metrics)

def metric_detail(metric_id):
    """Metric detail view."""
    metric = Metric.query.get_or_404(metric_id)
    return render_template('auth/metric-detail.html', metric=metric)

# Auth routes
def login():
    """User login view."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Welcome back!', 'success')
            return redirect(url_for('index'))
        
        flash('Invalid email or password', 'error')
    return render_template('auth/login.html')

def register():
    """User registration view."""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('auth.register'))

        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()

        flash('Registration successful', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')

def logout():
    """User logout view."""
    logout_user()
    flash('Successfully logged out', 'success')
    return redirect(url_for('index'))

# Admin routes
@admin_required
def admin_dashboard():
    """Admin dashboard view."""
    users_count = User.query.count()
    metrics_count = Metric.query.count()
    alerts_count = Alert.query.count()
    return render_template('admin/dashboard.html',
                         users_count=users_count,
                         metrics_count=metrics_count,
                         alerts_count=alerts_count)

@admin_required
def admin_users():
    """Admin users management view."""
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@admin_required
def admin_user_detail(user_id):
    """Admin user detail view."""
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.username = request.form.get('username')
        user.email = request.form.get('email')
        user.is_admin = 'is_admin' in request.form
        db.session.commit()
        flash('User updated successfully', 'success')
    return render_template('admin/user_detail.html', user=user)

@admin_required
def admin_user_delete(user_id):
    """Admin user deletion view."""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully', 'success')
    return redirect(url_for('admin.users'))

@admin_required
def admin_settings():
    """Admin settings view."""
    if request.method == 'POST':
        # Update system settings
        # Add your settings logic here
        flash('Settings updated successfully', 'success')
    return render_template('admin/settings.html')

# Metrics routes
@login_required
def create_metric():
    """Create metric view."""
    if request.method == 'POST':
        metric = Metric(
            name=request.form.get('name'),
            description=request.form.get('description'),
            type=request.form.get('type'),
            created_by=current_user.id
        )
        db.session.add(metric)
        db.session.commit()
        flash('Metric created successfully', 'success')
        return redirect(url_for('metrics.view_metric', metric_id=metric.id))
    return render_template('metrics/create.html')

@login_required
def update_metric(metric_id):
    """Update metric view."""
    metric = Metric.query.get_or_404(metric_id)
    if request.method == 'POST':
        metric.name = request.form.get('name')
        metric.description = request.form.get('description')
        db.session.commit()
        flash('Metric updated successfully', 'success')
        return redirect(url_for('metrics.view_metric', metric_id=metric.id))
    return render_template('metrics/update.html', metric=metric)

@login_required
def delete_metric(metric_id):
    """Delete metric view."""
    metric = Metric.query.get_or_404(metric_id)
    db.session.delete(metric)
    db.session.commit()
    flash('Metric deleted successfully', 'success')
    return redirect(url_for('index'))

@login_required
def update_metric_value(metric_id):
    """Update metric value view."""
    metric = Metric.query.get_or_404(metric_id)
    value = float(request.form.get('value'))
    
    # Check alerts
    alerts = Alert.query.filter_by(metric_id=metric_id).all()
    for alert in alerts:
        if alert.condition == 'greater_than' and value > alert.threshold:
            flash(f'Alert triggered: {alert.message}', 'warning')
        elif alert.condition == 'less_than' and value < alert.threshold:
            flash(f'Alert triggered: {alert.message}', 'warning')
    
    # Update metric value
    metric.current_value = value
    db.session.commit()
    return jsonify({'status': 'success'})

# Alert routes
@login_required
def create_alert(metric_id):
    """Create alert view."""
    if request.method == 'POST':
        alert = Alert(
            metric_id=metric_id,
            threshold=float(request.form.get('threshold')),
            condition=request.form.get('condition'),
            message=request.form.get('message'),
            created_by=current_user.id
        )
        db.session.add(alert)
        db.session.commit()
        flash('Alert created successfully', 'success')
        return redirect(url_for('metrics.view_metric', metric_id=metric_id))
    return render_template('metrics/create_alert.html', metric_id=metric_id)

@login_required
def update_alert(metric_id, alert_id):
    """Update alert view."""
    alert = Alert.query.get_or_404(alert_id)
    if request.method == 'POST':
        alert.threshold = float(request.form.get('threshold'))
        alert.condition = request.form.get('condition')
        alert.message = request.form.get('message')
        db.session.commit()
        flash('Alert updated successfully', 'success')
        return redirect(url_for('metrics.view_metric', metric_id=metric_id))
    return render_template('metrics/update_alert.html', alert=alert)

@login_required
def delete_alert(metric_id, alert_id):
    """Delete alert view."""
    alert = Alert.query.get_or_404(alert_id)
    db.session.delete(alert)
    db.session.commit()
    flash('Alert deleted successfully', 'success')
    return redirect(url_for('metrics.view_metric', metric_id=metric_id))

# Dashboard routes
@login_required
def view_dashboard(dashboard_id):
    """View dashboard view."""
    dashboard = Dashboard.query.get_or_404(dashboard_id)
    return render_template('dashboard/view.html', dashboard=dashboard)

@login_required
def create_dashboard():
    """Create dashboard view."""
    if request.method == 'POST':
        dashboard = Dashboard(
            name=request.form.get('name'),
            layout=request.form.get('layout'),
            created_by=current_user.id
        )
        db.session.add(dashboard)
        db.session.commit()
        flash('Dashboard created successfully', 'success')
        return redirect(url_for('dashboard.view_dashboard', dashboard_id=dashboard.id))
    return render_template('dashboard/create.html')

@login_required
def update_dashboard(dashboard_id):
    """Update dashboard view."""
    dashboard = Dashboard.query.get_or_404(dashboard_id)
    if request.method == 'POST':
        dashboard.name = request.form.get('name')
        db.session.commit()
        flash('Dashboard updated successfully', 'success')
        return redirect(url_for('dashboard.view_dashboard', dashboard_id=dashboard_id))
    return render_template('dashboard/update.html', dashboard=dashboard)

@login_required
def delete_dashboard(dashboard_id):
    """Delete dashboard view."""
    dashboard = Dashboard.query.get_or_404(dashboard_id)
    db.session.delete(dashboard)
    db.session.commit()
    flash('Dashboard deleted successfully', 'success')
    return redirect(url_for('index'))

@login_required
def save_dashboard_layout(dashboard_id):
    """Save dashboard layout view."""
    dashboard = Dashboard.query.get_or_404(dashboard_id)
    dashboard.layout = request.json.get('layout')
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Layout saved successfully'}) 