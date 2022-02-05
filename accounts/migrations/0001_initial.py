# Generated by Django 4.0.1 on 2022-02-05 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=255, null=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, null=True, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('teacher', models.BooleanField(default=False)),
                ('student', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
