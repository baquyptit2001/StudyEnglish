# Generated by Django 3.2.7 on 2021-10-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='static/app-assets/images/portrait/small', verbose_name='img'),
        ),
    ]
