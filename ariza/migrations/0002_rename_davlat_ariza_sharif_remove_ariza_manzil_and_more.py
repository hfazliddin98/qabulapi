# Generated by Django 5.0.7 on 2024-07-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ariza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ariza',
            old_name='davlat',
            new_name='sharif',
        ),
        migrations.RemoveField(
            model_name='ariza',
            name='manzil',
        ),
        migrations.RemoveField(
            model_name='ariza',
            name='viloyat',
        ),
        migrations.AddField(
            model_name='ariza',
            name='diplom',
            field=models.FileField(blank=True, upload_to='diplom'),
        ),
        migrations.AddField(
            model_name='ariza',
            name='pasport',
            field=models.FileField(blank=True, upload_to='pasport'),
        ),
    ]
