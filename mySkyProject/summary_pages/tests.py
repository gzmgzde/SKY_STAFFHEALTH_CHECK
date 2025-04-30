import unittest
from flask import url_for
from werkzeug.security import generate_password_hash
from summary_pages import create_app, db
from summary_pages.models import User, Metric, Alert, Dashboard

class TestConfig:
    """Test configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'test-key'

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self._create_test_data()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def _create_test_data(self):
        # Create test user
        user = User(
            username='testuser',
            email='test@example.com',
            password_hash=generate_password_hash('password123'),
            is_admin=False
        )
        admin = User(
            username='admin',
            email='admin@example.com',
            password_hash=generate_password_hash('admin123'),
            is_admin=True
        )
        db.session.add(user)
        db.session.add(admin)

        # Create test metric
        metric = Metric(
            name='Test Metric',
            description='Test Description',
            type='gauge',
            created_by=user.id
        )
        db.session.add(metric)

        # Create test alert
        alert = Alert(
            metric_id=1,
            threshold=80,
            condition='greater_than',
            message='Test Alert',
            created_by=user.id
        )
        db.session.add(alert)

        # Create test dashboard
        dashboard = Dashboard(
            name='Test Dashboard',
            layout='{"layout": "test"}',
            created_by=user.id
        )
        db.session.add(dashboard)
        
        db.session.commit()

class TestAuth(BaseTestCase):
    def test_login_success(self):
        """Test successful login."""
        response = self.client.post('/auth/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_login_failure(self):
        """Test failed login."""
        response = self.client.post('/auth/login', data={
            'email': 'test@example.com',
            'password': 'wrongpassword'
        }, follow_redirects=True)
        self.assertIn(b'Invalid email or password', response.data)

    def test_logout(self):
        """Test logout functionality."""
        # Login first
        self.client.post('/auth/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        })
        # Then logout
        response = self.client.get('/auth/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Successfully logged out', response.data)

class TestMetrics(BaseTestCase):
    def test_create_metric(self):
        """Test metric creation."""
        # Login as admin
        self.client.post('/auth/login', data={
            'email': 'admin@example.com',
            'password': 'admin123'
        })
        
        response = self.client.post('/metrics/create', data={
            'name': 'New Metric',
            'description': 'New Description',
            'type': 'gauge'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Metric created successfully', response.data)

    def test_view_metric_detail(self):
        """Test viewing metric details."""
        response = self.client.get('/metric/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Metric', response.data)

    def test_update_metric(self):
        """Test metric update."""
        # Login as admin
        self.client.post('/auth/login', data={
            'email': 'admin@example.com',
            'password': 'admin123'
        })
        
        response = self.client.post('/metrics/1/update', data={
            'name': 'Updated Metric',
            'description': 'Updated Description'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Metric updated successfully', response.data)

class TestAdmin(BaseTestCase):
    def test_admin_access(self):
        """Test admin panel access."""
        # Login as admin
        self.client.post('/auth/login', data={
            'email': 'admin@example.com',
            'password': 'admin123'
        })
        
        response = self.client.get('/admin/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Admin Dashboard', response.data)

    def test_non_admin_access(self):
        """Test admin panel access restriction."""
        # Login as regular user
        self.client.post('/auth/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        })
        
        response = self.client.get('/admin/dashboard')
        self.assertEqual(response.status_code, 403)

class TestAlerts(BaseTestCase):
    def test_create_alert(self):
        """Test alert creation."""
        # Login as admin
        self.client.post('/auth/login', data={
            'email': 'admin@example.com',
            'password': 'admin123'
        })
        
        response = self.client.post('/metrics/1/alerts/create', data={
            'threshold': 90,
            'condition': 'greater_than',
            'message': 'New Alert'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Alert created successfully', response.data)

    def test_alert_trigger(self):
        """Test alert triggering."""
        # Login as admin
        self.client.post('/auth/login', data={
            'email': 'admin@example.com',
            'password': 'admin123'
        })
        
        response = self.client.post('/metrics/1/update-value', data={
            'value': 85  # Above threshold of 80
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Alert triggered', response.data)

class TestDashboard(BaseTestCase):
    def test_save_dashboard_layout(self):
        """Test dashboard layout saving."""
        # Login as regular user
        self.client.post('/auth/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        })
        
        new_layout = {'layout': 'new test layout'}
        response = self.client.post('/dashboard/1/save-layout', 
            json=new_layout,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Layout saved successfully', response.data)

    def test_load_dashboard(self):
        """Test dashboard loading."""
        # Login as regular user
        self.client.post('/auth/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        })
        
        response = self.client.get('/dashboard/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Dashboard', response.data)

if __name__ == '__main__':
    unittest.main() 