# Generated by Django 3.0.8 on 2020-08-17 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tweet', '0035_auto_20200817_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='begeniSayisi',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='tweet',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='yorumSayisi',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='begeniSayisi',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='yorumSayisi',
        ),
    ]