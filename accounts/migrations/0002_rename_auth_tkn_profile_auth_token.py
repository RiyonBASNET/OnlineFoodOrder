# Generated by Django 4.0.6 on 2022-09-05 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='auth_tkn',
            new_name='auth_token',
        ),
    ]