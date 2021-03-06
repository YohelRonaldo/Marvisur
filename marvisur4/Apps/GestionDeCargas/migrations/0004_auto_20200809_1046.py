# Generated by Django 3.0.8 on 2020-08-09 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDeCargas', '0003_auto_20200808_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinatario',
            name='id',
        ),
        migrations.RemoveField(
            model_name='encomienda',
            name='id',
        ),
        migrations.RemoveField(
            model_name='guiaremision',
            name='id',
        ),
        migrations.RemoveField(
            model_name='movilidad',
            name='id',
        ),
        migrations.RemoveField(
            model_name='remitente',
            name='id',
        ),
        migrations.AddField(
            model_name='destinatario',
            name='iddest',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='encomienda',
            name='idenco',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guiaremision',
            name='idguia',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movilidad',
            name='idmovi',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='remitente',
            name='idremi',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
