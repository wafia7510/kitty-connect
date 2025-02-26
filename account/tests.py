from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.
class AccountViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
    
    def test_login_view(self):
        """Test that the login page loads properly."""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_dashboard_redirect(self):
        """Test that an authenticated user can access the dashboard."""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/dashboard.html')



