# Generated by Django 3.1.6 on 2021-02-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
    ]