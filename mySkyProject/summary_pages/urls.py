from flask import Blueprint
from . import views

# Create blueprints
main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
metrics_bp = Blueprint('metrics', __name__, url_prefix='/metrics')
dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# Main routes
main_bp.add_url_rule('/', view_func=views.index, methods=['GET'])
main_bp.add_url_rule('/metric/<int:metric_id>', view_func=views.metric_detail, methods=['GET'])

# Auth routes
auth_bp.add_url_rule('/login', view_func=views.login, methods=['GET', 'POST'])
auth_bp.add_url_rule('/register', view_func=views.register, methods=['GET', 'POST'])
auth_bp.add_url_rule('/logout', view_func=views.logout, methods=['GET'])

# Admin routes
admin_bp.add_url_rule('/dashboard', view_func=views.admin_dashboard, methods=['GET'])
admin_bp.add_url_rule('/users', view_func=views.admin_users, methods=['GET'])
admin_bp.add_url_rule('/users/<int:user_id>', view_func=views.admin_user_detail, methods=['GET', 'POST'])
admin_bp.add_url_rule('/users/<int:user_id>/delete', view_func=views.admin_user_delete, methods=['POST'])
admin_bp.add_url_rule('/settings', view_func=views.admin_settings, methods=['GET', 'POST'])

# Metrics routes
metrics_bp.add_url_rule('/create', view_func=views.create_metric, methods=['GET', 'POST'])
metrics_bp.add_url_rule('/<int:metric_id>/update', view_func=views.update_metric, methods=['GET', 'POST'])
metrics_bp.add_url_rule('/<int:metric_id>/delete', view_func=views.delete_metric, methods=['POST'])
metrics_bp.add_url_rule('/<int:metric_id>/update-value', view_func=views.update_metric_value, methods=['POST'])
metrics_bp.add_url_rule('/<int:metric_id>/alerts/create', view_func=views.create_alert, methods=['GET', 'POST'])
metrics_bp.add_url_rule('/<int:metric_id>/alerts/<int:alert_id>/update', view_func=views.update_alert, methods=['GET', 'POST'])
metrics_bp.add_url_rule('/<int:metric_id>/alerts/<int:alert_id>/delete', view_func=views.delete_alert, methods=['POST'])

# Dashboard routes
dashboard_bp.add_url_rule('/<int:dashboard_id>', view_func=views.view_dashboard, methods=['GET'])
dashboard_bp.add_url_rule('/create', view_func=views.create_dashboard, methods=['GET', 'POST'])
dashboard_bp.add_url_rule('/<int:dashboard_id>/update', view_func=views.update_dashboard, methods=['GET', 'POST'])
dashboard_bp.add_url_rule('/<int:dashboard_id>/delete', view_func=views.delete_dashboard, methods=['POST'])
dashboard_bp.add_url_rule('/<int:dashboard_id>/save-layout', view_func=views.save_dashboard_layout, methods=['POST']) 