# Generated by Django 5.0.2 on 2024-02-12 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]