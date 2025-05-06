from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='1234')
        self.client = APIClient()
        self.client.login(username='testuser', password='1234')


    def test_product_creation(self):

        product = Product.objects.create(
        name='Test Product',
        price=99.99,
        stock=10,
        owner=self.user
        )
        self.assertEqual(product.name, "Test Product")  # Check if the product name is correct
        self.assertEqual(product.owner.username, "testuser")  # Check if the product count increased by 1

    def test_api_list_requires_auth(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 401)

    def test_api_with_jwt(self):
        from rest_framework_simplejwt.tokens import RefreshToken
        token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)

