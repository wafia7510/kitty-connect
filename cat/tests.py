
# Create your tests here.
from django.test import TestCase, Client
from .models import Cat
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cat.views import cat_list, cat_create
class CatModelTest(TestCase):
    def setUp(self):
        self.cat = Cat.objects.create(
            name="Whiskers",
            breed="Persian",
            age=3,
            description="A cute and fluffy Persian cat."
        )

    def test_cat_creation(self):
        """Test that a Cat object is created correctly."""
        self.assertEqual(self.cat.name, "Whiskers")
        self.assertEqual(self.cat.breed, "Persian")
        self.assertEqual(self.cat.age, 3)

    def test_string_representation(self):
        """Test the string representation of the Cat model."""
        self.assertEqual(str(self.cat), "Whiskers")

    class CatsURLTest(SimpleTestCase):
        def test_cat_list_url_resolves(self):
            """Test that the cat list URL resolves correctly."""
            url = reverse("cat_list")
            self.assertEqual(resolve(url).func, cat_list)

        def test_cat_create_url_resolves(self):
            """Test that the cat create URL resolves correctly."""
            url = reverse("cat_create")
            self.assertEqual(resolve(url).func, cat_create)

    class CatsTemplateTest(TestCase):
        def setUp(self):
            self.client = Client()

        def test_cat_list_template(self):
            """Test that the cat list page loads correctly."""
            response = self.client.get(reverse('cat_list'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'cat/cat_list.html')