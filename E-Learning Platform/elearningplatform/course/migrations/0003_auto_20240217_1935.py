# Generated by Django 3.1.3 on 2024-02-17 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_appuser_profilepic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='organisation',
            new_name='email',
        ),
    ]