# Generated by Django 3.1.5 on 2021-02-06 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adopter',
            name='adress',
        ),
        migrations.AddField(
            model_name='adopter',
            name='city',
            field=models.CharField(default='s', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adopter',
            name='neighbourhood',
            field=models.CharField(default='s', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adopter',
            name='number',
            field=models.CharField(default='s', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adopter',
            name='state',
            field=models.CharField(default='s', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adopter',
            name='street',
            field=models.CharField(default='s', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adopter',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]