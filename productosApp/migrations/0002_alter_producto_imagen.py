# Generated by Django 3.2.8 on 2022-01-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productosApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='productos'),
        ),
    ]