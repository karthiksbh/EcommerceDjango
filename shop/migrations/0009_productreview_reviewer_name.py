# Generated by Django 3.2.5 on 2021-08-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_rename_status_productreview_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='reviewer_name',
            field=models.CharField(default='change', max_length=200),
        ),
    ]
