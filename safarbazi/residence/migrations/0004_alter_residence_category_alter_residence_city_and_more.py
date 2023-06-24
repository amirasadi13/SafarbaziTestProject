# Generated by Django 4.0.7 on 2023-06-23 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('residence', '0003_alter_calendar_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residence',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='residence.category'),
        ),
        migrations.AlterField(
            model_name='residence',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.city'),
        ),
        migrations.AlterField(
            model_name='residence',
            name='latitude',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='residence',
            name='longitude',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='residence',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.province'),
        ),
    ]