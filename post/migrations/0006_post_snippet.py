# Generated by Django 3.1.6 on 2021-02-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20210211_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click the post to read the post...', max_length=255),
        ),
    ]
