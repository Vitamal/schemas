from django.test import RequestFactory, TestCase

from csv_generator.models import User


class TestSchemasListView(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com', password='top_secret')
