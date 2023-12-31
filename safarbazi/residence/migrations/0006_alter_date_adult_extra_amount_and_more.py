# Generated by Django 4.0.7 on 2023-06-23 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residence', '0005_alter_date_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='adult_extra_amount',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='baby_extra_amount',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='base_amount',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='child_extra_amount',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
