from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    metrics = db.relationship('Metric', backref='author', lazy='dynamic')
    alerts = db.relationship('Alert', backref='author', lazy='dynamic')
    dashboards = db.relationship('Dashboard', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256))
    current_value = db.Column(db.Float)
    target_value = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    alerts = db.relationship('Alert', backref='metric', lazy='dynamic')
    dashboards = db.relationship('DashboardMetric', backref='metric', lazy='dynamic')

    def __repr__(self):
        return f'<Metric {self.name}>'

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    metric_id = db.Column(db.Integer, db.ForeignKey('metric.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    threshold = db.Column(db.Float, nullable=False)
    condition = db.Column(db.String(32), nullable=False)  # 'above' or 'below'
    message = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Alert {self.metric.name} {self.condition} {self.threshold}>'

class Dashboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    layout = db.Column(db.JSON)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Dashboard {self.name}>'

class DashboardMetric(db.Model):
    dashboard_id = db.Column(db.Integer, db.ForeignKey('dashboard.id'), primary_key=True)
    metric_id = db.Column(db.Integer, db.ForeignKey('metric.id'), primary_key=True)
    position = db.Column(db.Integer)  # Order in the dashboard
    size = db.Column(db.String(20))  # Size of the metric widget (small, medium, large)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id)) 