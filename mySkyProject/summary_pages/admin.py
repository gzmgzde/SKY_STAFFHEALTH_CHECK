from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import db
from .models import User, Metric, Alert
from .forms import RegistrationForm

bp = Blueprint('admin', __name__)

def admin_required(f):
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('You do not have permission to access this page.')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@bp.route('/admin')
@login_required
@admin_required
def dashboard():
    users = User.query.count()
    metrics = Metric.query.count()
    alerts = Alert.query.count()
    return render_template('admin/dashboard.html', title='Admin Dashboard',
                         users=users, metrics=metrics, alerts=alerts)

@bp.route('/admin/users')
@login_required
@admin_required
def users():
    users = User.query.all()
    return render_template('admin/users.html', title='User Management', users=users)

@bp.route('/admin/users/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.is_admin = request.form.get('is_admin') == 'true'
        db.session.add(user)
        db.session.commit()
        flash('User has been created!')
        return redirect(url_for('admin.users'))
    return render_template('admin/create_user.html', title='Create User', form=form)

@bp.route('/admin/metrics')
@login_required
@admin_required
def metrics():
    metrics = Metric.query.all()
    return render_template('admin/metrics.html', title='Metric Management', metrics=metrics)

@bp.route('/admin/alerts')
@login_required
@admin_required
def alerts():
    alerts = Alert.query.all()
    return render_template('admin/alerts.html', title='Alert Management', alerts=alerts) 