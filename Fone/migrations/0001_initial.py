# Generated by Django 4.1.4 on 2022-12-14 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Circuits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circuits_Name', models.CharField(default='Car Name', max_length=255)),
                ('circuits_length', models.CharField(default='Car Model', max_length=255)),
                ('circuits_laps', models.CharField(default='Factory', max_length=255)),
                ('circuits_distance', models.IntegerField()),
                ('circuits_speed', models.IntegerField()),
                ('circuits_city', models.CharField(default='Founder', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Fone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carName', models.CharField(default='Car Name', max_length=255)),
                ('carModel', models.CharField(default='Car Model', max_length=255)),
                ('carFactory', models.CharField(default='Factory', max_length=255)),
                ('ratingDriver', models.IntegerField()),
                ('trophyDriver', models.IntegerField()),
                ('founder', models.CharField(default='Founder', max_length=256)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
