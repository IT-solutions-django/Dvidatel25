# Generated by Django 5.2 on 2025-04-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_companyinfo_about_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='why_it_is_cheaper_to_repair',
            field=models.TextField(default='', verbose_name='Почему выгоднее чинить'),
            preserve_default=False,
        ),
    ]
