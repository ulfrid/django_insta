# Generated by Django 3.0.8 on 2020-08-01 14:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follower_set',
            field=models.ManyToManyField(blank=True, related_name='_user_follower_set_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='following_set',
            field=models.ManyToManyField(blank=True, related_name='_user_following_set_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
