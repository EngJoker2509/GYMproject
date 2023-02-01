# Generated by Django 4.1.5 on 2023-01-29 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gymUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45, null=True)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.IntegerField()),
                ('regNum', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('password', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participantName', models.CharField(max_length=45, null=True)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=45)),
                ('legalNumber', models.IntegerField()),
                ('phoneNumber', models.IntegerField(null=True)),
                ('midicalHistory', models.TextField(max_length=255, null=True)),
                ('gymUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gymUser_par_id', to='GYMapp.gymusers')),
            ],
        ),
        migrations.CreateModel(
            name='subScriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('_from', models.DateTimeField(auto_now_add=True)),
                ('_to', models.DateTimeField(auto_now=True)),
                ('active', models.IntegerField(default=0)),
                ('gymUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gymUser_sub_id', to='GYMapp.gymusers')),
                ('participantUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participantUser_id', to='GYMapp.participants')),
            ],
        ),
    ]