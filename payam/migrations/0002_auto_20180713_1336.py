# Generated by Django 2.0.7 on 2018-07-13 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payam', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payam',
            options={'ordering': ['-time']},
        ),
    ]
