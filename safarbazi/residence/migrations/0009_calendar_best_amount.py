# Generated by Django 4.0.7 on 2023-06-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residence', '0008_alter_date_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='best_amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
