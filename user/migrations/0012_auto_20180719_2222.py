# Generated by Django 2.0.7 on 2018-07-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_users_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='color',
            field=models.CharField(default='a80000', help_text='giv me a hex color number to set :)', max_length=120),
        ),
    ]