# Generated by Django 3.0.8 on 2020-08-17 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tweet', '0029_auto_20200817_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Tweet.Tweet'),
        ),
    ]
