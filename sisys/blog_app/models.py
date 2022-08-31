from django.db import models

from sisys.sisis_auth.models import SisisUser


class Category(models.Model):
    name = models.Choices


class Tags(models.Model):
    name = models.Choices
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    pass


class Like(models.Model):
    pass


class Post(models.Model):
    author = models.ForeignKey(
        SisisUser,
        on_delete=models.CASCADE,
    )
    pictures = models.ImageField(upload_to='blog_pics')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.ForeignKey(Like, on_delete=models.CASCADE)
