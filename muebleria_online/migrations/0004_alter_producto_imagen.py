# Generated by Django 5.1.6 on 2025-02-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muebleria_online', '0003_alter_categoria_options_alter_producto_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
