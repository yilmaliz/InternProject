# Generated by Django 3.0.8 on 2020-08-15 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tweet', '0015_auto_20200814_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
            ],
        ),
    ]
