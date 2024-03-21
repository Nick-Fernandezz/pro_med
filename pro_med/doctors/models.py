from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Doctors(AbstractUser):

    avatar = models.ImageField('Фото', upload_to='pacients/%Y/%Y/%m/%d/%H-%M-%S/', null=True, blank=True)
    
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100, null=True, blank=True)

    birthday = models.DateField('Дата рождения', null=True)

    specialization = models.CharField('Специализация', max_length=100, null=True)
    position = models.CharField('Должность', max_length=200, default=None, null=True)

    education_place = models.CharField('Учебное заведение получения образования', max_length=300, null=True)
    education_end_year = models.IntegerField('Год окончания', null=True)

    seniority = models.IntegerField('Стаж', null=True)

    series_passport = models.IntegerField('Серия паспорта', null=True)
    numner_passport = models.IntegerField('Номер паспорта', null=True)

    sex = models.CharField('Пол', choices=(( 'Male', 'Мужской'), ('Female', 'Женский')), max_length=10, null=True)

    country = models.CharField('Страна', max_length=100, default='Россия', null=True)
    state = models.CharField('Субъект', max_length=150, help_text='Край, область', null=True)
    city = models.CharField('Город', max_length=100, null=True)
    street = models.CharField('Улица', max_length=200, null=True, blank=True)
    house = models.CharField('Дом', max_length=20, null=True)
    entrance =  models.CharField('Подъезд', max_length=10, null=True, blank=True)
    apartment = models.CharField('Квартира', max_length=10, null=True, blank=True)

    phone_number = models.CharField('Телефон', max_length=15, null=True)
    email = models.CharField('Почта', max_length=100, null=True)

    class Meta:
        verbose_name = "врач"
        verbose_name_plural = "Врачи"
