# Generated by Django 5.0.3 on 2024-03-21 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacients', '0003_alter_therapeuticanddiagnosticevents_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacients',
            name='insurance_company',
            field=models.CharField(max_length=150, null=True, verbose_name='Страховая компания'),
        ),
        migrations.AddField(
            model_name='pacients',
            name='insurance_end_date',
            field=models.DateField(null=True, verbose_name='Срок действия'),
        ),
        migrations.AddField(
            model_name='pacients',
            name='insurance_number',
            field=models.IntegerField(null=True, verbose_name='Cтраховой полис'),
        ),
    ]