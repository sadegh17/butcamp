# Generated by Django 2.0.7 on 2018-07-11 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
