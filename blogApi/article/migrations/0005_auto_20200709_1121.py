# Generated by Django 3.0.8 on 2020-07-09 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20200709_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='file',
            new_name='image',
        ),
    ]
