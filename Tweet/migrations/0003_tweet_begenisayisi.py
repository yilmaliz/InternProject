# Generated by Django 3.0.8 on 2020-07-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tweet', '0002_auto_20200720_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='begeniSayisi',
            field=models.IntegerField(default=0),
        ),
    ]
