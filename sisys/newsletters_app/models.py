import markdown2 as markdown2
from django.db import models


class NewsletterUser(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    time_added = models.DateTimeField(auto_now_add=True)
    verbose_name = "User/'s email",

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(
        max_length=3200,
        verbose_name='Markdown\'s Content',
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    @property
    def html_content(self):
        markdown = markdown2.Markdown()
        return markdown.convert(self.content)
