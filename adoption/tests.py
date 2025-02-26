from django.test import TestCase
from django.contrib.auth.models import User
from .models import AdoptionRequest
from cat.models import Cat
# Create your tests here.
class AdoptionRequestModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.cat = Cat.objects.create(name="Simba", breed="Siamese", age=2)
        self.adoption_request = AdoptionRequest.objects.create(
            user=self.user,
            cat=self.cat,
            message="I love cats and want to adopt Simba.",
            status="Pending"
        )

    def test_adoption_request_creation(self):
        """Test that an adoption request is created correctly."""
        self.assertEqual(self.adoption_request.user.username, "testuser")
        self.assertEqual(self.adoption_request.cat.name, "Simba")
        self.assertEqual(self.adoption_request.status, "Pending")


