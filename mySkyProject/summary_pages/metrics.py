from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import db
from .models import Metric, Alert
from .forms import MetricForm, AlertForm

bp = Blueprint('metrics', __name__)

@bp.route('/metrics')
@login_required
def list_metrics():
    metrics = Metric.query.filter_by(user_id=current_user.id).all()
    return render_template('metrics/list.html', title='My Metrics', metrics=metrics)

@bp.route('/metrics/create', methods=['GET', 'POST'])
@login_required
def create_metric():
    form = MetricForm()
    if form.validate_on_submit():
        metric = Metric(name=form.name.data, value=form.value.data, user_id=current_user.id)
        db.session.add(metric)
        db.session.commit()
        flash('Your metric has been recorded!')
        return redirect(url_for('metrics.list_metrics'))
    return render_template('metrics/create.html', title='Record Metric', form=form)

@bp.route('/metrics/<int:id>/alerts', methods=['GET', 'POST'])
@login_required
def create_alert(id):
    metric = Metric.query.get_or_404(id)
    if metric.user_id != current_user.id:
        flash('You do not have permission to create alerts for this metric.')
        return redirect(url_for('metrics.list_metrics'))
    
    form = AlertForm()
    if form.validate_on_submit():
        alert = Alert(threshold=form.threshold.data, condition=form.condition.data,
                     metric_id=metric.id, user_id=current_user.id)
        db.session.add(alert)
        db.session.commit()
        flash('Your alert has been created!')
        return redirect(url_for('metrics.list_metrics'))
    return render_template('metrics/create_alert.html', title='Create Alert', form=form, metric=metric) 