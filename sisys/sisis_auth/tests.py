from django.contrib.auth import get_user_model
from django.test import TestCase, Client


from sisis_auth.models import Profile
UserModel = get_user_model()


class CreateUserTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.email = 'pesho@abc.it'
        self.password = '1234qwer'

    def test_check_createdUser__shouldCreateProfileToo(self):
        self.user = UserModel.objects.create_user(email=self.email, password=self.password)
        self.client.force_login(self.user)
        self.profile = Profile.objects.get(pk=self.user.id)
        self.assertEqual(self.user.id, self.profile.user_id)

    def test_check_userCreated(self):
        response = self.client.post('/accounts/register/?next=/accounts/email-confirmation/', kwargs={'email': self.email, 'password1': self.password, 'password2': self.password})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('accounts/activate-your-account.html')


class ProfileTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='pesho@abc.it', password='1234qwer')

    def test_profile_rendered_in_correct_template(self):
        self.client.force_login(self.user)
        self.client.get('/accounts/profile/')
        self.assertTemplateUsed('accounts/profile_details.html')










