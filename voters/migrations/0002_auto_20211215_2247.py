# Generated by Django 3.1.4 on 2021-12-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='sl',
            field=models.IntegerField(max_length=200),
        ),
    ]
