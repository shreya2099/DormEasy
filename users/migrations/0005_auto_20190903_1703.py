# Generated by Django 2.2.4 on 2019-09-03 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190903_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reg_students',
            old_name='Gender',
            new_name='gender',
        ),
    ]
