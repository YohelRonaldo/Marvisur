# Generated by Django 3.0.8 on 2020-08-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDeCargas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codigoqr',
            name='Imagen',
        ),
        migrations.AddField(
            model_name='codigoqr',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
    ]
