from django.test import TestCase
from users.models import User
from django.core.exceptions import ValidationError

class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username='fabiojulio',
            name='Fábio Júlio',
            email='fabiojulio@gmail.com',
            password='teste'
        )

    def test_user_empty_fields(self):
        user = User.objects.get(username='fabiojulio')
        self.assertEqual(user.username, 'fabiojulio')
        self.assertEqual(user.name, 'Fábio Júlio')
        self.assertEqual(user.email, 'fabiojulio@gmail.com')
        self.assertEqual(user.password, 'teste')

    def test_user_submiting_an_invalid_email(self):
        user = self.user
        user.email = 'aaa'  # Define um email inválido
        with self.assertRaises(ValidationError):
            user.full_clean()
