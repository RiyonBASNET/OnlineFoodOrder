# Generated by Django 4.0.6 on 2022-09-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userspage', '0004_alter_order_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
