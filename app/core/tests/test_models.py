from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

# create users in our tests
def create_sample_user(email='test@cleandev.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)



class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@javid.com'
        password = 'password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password)) # check_password comes with django

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized - all lower string"""
        email = 'test@Javid.com'
        user = get_user_model().objects.create_user(email, 'password123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user w/o email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password123')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'test@javid.com',
            'password123'
        )
        self.assertTrue(user.is_superuser) # included as part of PermissionsMixin
        self.assertTrue(user.is_staff)

    def test_tag_is_created_and_converts_to_correct_string_representation(self):
        # create our tag
            # give it a name we may use in our system
        tag = models.Tag.objects.create(
            user=create_sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)