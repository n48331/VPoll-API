# Generated by Django 3.1.4 on 2021-12-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0002_auto_20211215_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='sl',
            field=models.IntegerField(),
        ),
    ]
