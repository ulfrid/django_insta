# Generated by Django 3.0.8 on 2020-08-01 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200801_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='accounts/avatar/%Y/%m/%d'),
        ),
    ]
