# Generated by Django 5.0.6 on 2024-05-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0003_alter_cliente_numero_visitas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='numero_visitas',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
