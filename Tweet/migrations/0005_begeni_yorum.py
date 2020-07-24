# Generated by Django 3.0.8 on 2020-07-23 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tweet', '0004_tweet_yorumsayisi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Begeni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetId', models.IntegerField(default=0)),
                ('kullanıcıId', models.IntegerField(default=1996)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetId', models.IntegerField(default=0)),
                ('kullanıcıId', models.IntegerField(default=1996)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]