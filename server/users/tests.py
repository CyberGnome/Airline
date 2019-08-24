from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class UsersManagersTests(TestCase):
    def test_create_superuser(self):
        User = get_user_model()

        admin_user = User.objects.create_superuser('admin@airline.local', 'admin')
        self.assertEqual(admin_user.email, 'admin@airline.local')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='admin@airline.local', password='admin', is_superuser=False)

    def test_create_users(self):
        for i in range(1, 10):
            User = get_user_model()

            user = User.objects.create_user(email='user%d@airline.local' % i, password='user%d' % i)
            self.assertEqual(user.email, 'user%d@airline.local' % i)
            self.assertTrue(user.is_active)
            self.assertFalse(user.is_staff)
            self.assertFalse(user.is_superuser)
            try:
                self.assertIsNone(user.username)
            except AttributeError:
                pass
            with self.assertRaises(TypeError):
                User.objects.create_user()
            with self.assertRaises(TypeError):
                User.objects.create_user(email='')
            with self.assertRaises(ValueError):
                User.objects.create_user(email='', password='user%d' % i)
