# Generated by Django 4.0.7 on 2022-09-11 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0002_item_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
