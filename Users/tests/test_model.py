from django.test import TestCase
from Users.models import MyUser


class MyUserTestCase(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create(username='testuser', password='testpass')

    # Test avatar image field.
    def test_avatar_upload_to(self):
        upload_to = self.user._meta.get_field('avatar').upload_to
        self.assertEqual(upload_to, 'avatar')

    def test_avatar_null(self):
        null = self.user._meta.get_field('avatar').null
        self.assertEqual(null, True)

    def test_avatar_blank(self):
        blank = self.user._meta.get_field('avatar').blank
        self.assertEqual(blank, True)

    # Test city char field.
    def test_city_max_length(self):
        max_length = self.user._meta.get_field('city').max_length
        self.assertEqual(max_length, 100)

    def test_city_blank(self):
        blank = self.user._meta.get_field('city').blank
        self.assertEqual(blank, True)

    # Test country char field.
    def test_country_max_length(self):
        max_length = self.user._meta.get_field('country').max_length
        self.assertEqual(max_length, 100)

    def test_country_blank(self):
        blank = self.user._meta.get_field('country').blank
        self.assertEqual(blank, True)

    # Test bio text field.
    def test_bio_max_length(self):
        max_length = self.user._meta.get_field('bio').max_length
        self.assertEqual(max_length, 1000)

    def test_bio_blank(self):
        blank = self.user._meta.get_field('bio').blank
        self.assertEqual(blank, True)

    # Test friends many to many field.
    def test_friends_related_model(self):
        related_model = self.user._meta.get_field('friends').related_model
        self.assertEqual(related_model, MyUser)

    def test_friends_blank(self):
        blank = self.user._meta.get_field('friends').blank
        self.assertEqual(blank, True)

    # Test __str__ function.
    def test_str_function(self):
        str = self.user.__str__()
        self.assertEqual(str, self.user.username)
