# Generated by Django 3.1.3 on 2024-02-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20240217_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='email',
        ),
        migrations.AddField(
            model_name='appuser',
            name='hpNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]