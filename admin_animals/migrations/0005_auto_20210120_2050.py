# Generated by Django 3.1.5 on 2021-01-20 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_animals', '0004_auto_20210120_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='castrated',
            new_name='is_adopted',
        ),
        migrations.AddField(
            model_name='animal',
            name='is_castrated',
            field=models.BooleanField(default=False),
        ),
    ]
