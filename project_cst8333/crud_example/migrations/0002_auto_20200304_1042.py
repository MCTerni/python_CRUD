# Generated by Django 3.0.2 on 2020-03-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='ref_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='records',
            name='scalar_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='records',
            name='uom_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='records',
            name='value',
            field=models.IntegerField(),
        ),
    ]
