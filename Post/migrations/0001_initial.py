# Generated by Django 4.1.1 on 2022-09-22 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=pathlib.PureWindowsPath('C:/Users/Lucas/Desktop/Programming/PostAutomator/PostAutomate/media'))),
                ('post_date', models.DateTimeField(blank=True, null=True)),
                ('facebook', models.BooleanField(default=False)),
                ('instagram', models.BooleanField(default=False)),
                ('twitter', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
