# Generated by Django 5.2 on 2025-04-30 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_privacypolicy'),
    ]

    operations = [
        migrations.AddField(
            model_name='privacypolicy',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='privacy_policy/', verbose_name='Файл'),
        ),
    ]
