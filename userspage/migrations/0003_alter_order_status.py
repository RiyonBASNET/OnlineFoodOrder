# Generated by Django 4.0.6 on 2022-08-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userspage', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Pending', max_length=200, null=True),
        ),
    ]
