from django.contrib.auth import get_user_model
from django.template import context
from django.test import TestCase, Client
from django.urls import reverse

from sisis_auth.models import Profile

UserModel = get_user_model()


class CreateUserTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.email = 'pesho@abc.it'
        self.password = '1234qwer'

    def test_check_createdUser__shouldHaveProfile(self):
        self.user = UserModel.objects.create_user(email=self.email, password=self.password)
        self.client.force_login(self.user)
        self.profile = Profile.objects.get(pk=self.user.id)
        self.assertEqual(self.user.id, self.profile.user_id)


class ViewAccountTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='pesho@abc.it', password='1234qwer')

    def test_userShouldSeeAccount__whenLoggedIn(self):
        self.client.login(email='pesho@abc.it', password='1234qwer')
        response = self.client.get(reverse('my account'))
        profile = response.context['profile']
        print(profile)



