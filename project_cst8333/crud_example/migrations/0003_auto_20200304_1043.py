# Generated by Django 3.0.2 on 2020-03-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_example', '0002_auto_20200304_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='decimals',
            field=models.IntegerField(),
        ),
    ]
