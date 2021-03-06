# Generated by Django 3.2.7 on 2021-10-18 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=15)),
                ('language', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=15)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
