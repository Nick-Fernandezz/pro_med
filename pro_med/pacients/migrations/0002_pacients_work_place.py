# Generated by Django 5.0.3 on 2024-03-20 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacients',
            name='work_place',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Место работы'),
        ),
    ]
