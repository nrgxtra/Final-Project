# Generated by Django 4.0.7 on 2022-09-23 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='pet',
            new_name='post',
        ),
    ]
