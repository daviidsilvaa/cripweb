# Generated by Django 2.2.2 on 2019-06-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criptografia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='C:\\Users\\gabriel\\Desktop\\UFOP\\Programação Web\\cripweb\\cripweb\\static/media'),
        ),
    ]
