# Generated by Django 5.0.2 on 2024-02-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='image_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]