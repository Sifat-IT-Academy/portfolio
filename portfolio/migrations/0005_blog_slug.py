# Generated by Django 5.0.6 on 2024-07-05 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
