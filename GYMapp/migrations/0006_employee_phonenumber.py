# Generated by Django 3.2.16 on 2023-02-04 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GYMapp', '0005_alter_subscription__to'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phonenumber',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
