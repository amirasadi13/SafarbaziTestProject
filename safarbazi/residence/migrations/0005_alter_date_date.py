# Generated by Django 4.0.7 on 2023-06-23 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residence', '0004_alter_residence_category_alter_residence_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.DateField(),
        ),
    ]
