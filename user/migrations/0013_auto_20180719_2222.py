# Generated by Django 2.0.7 on 2018-07-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20180719_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='color',
            field=models.CharField(default='a80000', help_text='give me a hex color number to set :)', max_length=120),
        ),
    ]
