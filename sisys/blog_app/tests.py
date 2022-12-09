from django.test import TestCase, Client
from blog_app.models import Post
from sisis_auth.models import SisisUser


class BlogTest(TestCase):
    def setUp(self) -> None:
        self.user = SisisUser.objects.create_user(email='pesho@abc.it', password='1234qwer')
        self.writer = SisisUser.objects.create_user(email='gosho@abc.it', password='1234qwer')
        self.client = Client()
        self.post = Post.objects.create(title='test',
                                        slug='test',
                                        author=self.writer,
                                        content='test content',
                                        )

    def test_everyone_can_see_post(self):
        response = self.client.get('/blog/post/1/test')
        self.assertTrue(response.context['post'], self.post)

    def test_only_author_can_edit_his_post(self):
        response = self.client.get('/blog/post-update/1/test')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('accounts/login.html')

        self.client.force_login(self.writer)
        response = self.client.get('/blog/post-update/1/test')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('blog/post-update.html')

    def test_only_author_can_delete_his_post(self):
        response = self.client.get('/blog/post-delete/1/test')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('accounts/login.html')

        self.client.force_login(self.writer)
        response = self.client.get('/blog/post-delete/1/test')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('blog/blog.html')

