# Generated by Django 3.2.5 on 2021-08-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210820_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_left',
            field=models.PositiveIntegerField(),
        ),
    ]
