# Generated by Django 4.0.7 on 2023-06-23 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('residence', '0002_remove_date_residence_d_date_d1c165_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='room',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='residence.room'),
        ),
    ]