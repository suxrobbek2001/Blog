# Generated by Django 3.2.8 on 2021-12-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_rasm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rasm',
            name='photo',
            field=models.FileField(upload_to='static/media/'),
        ),
    ]