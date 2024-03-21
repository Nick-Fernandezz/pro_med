from django.db import models

# Create your models here.

class Doctors(models.Model):

    avatar = models.ImageField('Фото', upload_to='pacients/%Y/%Y/%m/%d/%H-%M-%S/', null=True, blank=True)
    
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100, null=True, blank=True)

    birthday = models.DateField('Дата рождения')

    specialization = models.CharField('Специализация', max_length=100)
    position = models.CharField('Должность', max_length=200, default=None)

    education_place = models.CharField('Учебное заведение получения образования', max_length=300)
    education_end_year = models.IntegerField('Год окончания')

    seniority = models.IntegerField('Стаж')

    series_passport = models.IntegerField('Серия паспорта')
    numner_passport = models.IntegerField('Номер паспорта')

    sex = models.CharField('Пол', choices=(( 'Male', 'Мужской'), ('Female', 'Женский')), max_length=10)

    country = models.CharField('Страна', max_length=100, default='Россия')
    state = models.CharField('Субъект', max_length=150, help_text='Край, область')
    city = models.CharField('Город', max_length=100)
    street = models.CharField('Улица', max_length=200, null=True, blank=True)
    house = models.CharField('Дом', max_length=20)
    entrance =  models.CharField('Подъезд', max_length=10, null=True, blank=True)
    apartment = models.CharField('Квартира', max_length=10, null=True, blank=True)

    phone_number = models.CharField('Телефон', max_length=15)
    email = models.CharField('Почта', max_length=100)
