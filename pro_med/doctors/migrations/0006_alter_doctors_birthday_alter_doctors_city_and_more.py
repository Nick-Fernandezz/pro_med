# Generated by Django 5.0.3 on 2024-03-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_rename_doctor_doctors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='country',
            field=models.CharField(default='Россия', max_length=100, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='education_end_year',
            field=models.IntegerField(null=True, verbose_name='Год окончания'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='education_place',
            field=models.CharField(max_length=300, null=True, verbose_name='Учебное заведение получения образования'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='email',
            field=models.CharField(max_length=100, null=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='house',
            field=models.CharField(max_length=20, null=True, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='numner_passport',
            field=models.IntegerField(null=True, verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='seniority',
            field=models.IntegerField(null=True, verbose_name='Стаж'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='series_passport',
            field=models.IntegerField(null=True, verbose_name='Серия паспорта'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='sex',
            field=models.CharField(choices=[('Male', 'Мужской'), ('Female', 'Женский')], max_length=10, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='specialization',
            field=models.CharField(max_length=100, null=True, verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='state',
            field=models.CharField(help_text='Край, область', max_length=150, null=True, verbose_name='Субъект'),
        ),
    ]
