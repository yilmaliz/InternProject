# Generated by Django 3.0.8 on 2020-08-17 13:29

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Tweet', '0024_auto_20200817_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.fields.IntegerField, to='Tweet.Tweet'),
        ),
    ]
