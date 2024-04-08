from django.db import models

from doctors.models import Doctors

# Create your models here.

class Pacients(models.Model):

    avatar = models.ImageField('Фото', upload_to='pacients/%Y/%Y/%m/%d/%H-%M-%S/', null=True, blank=True)
    
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100, null=True, blank=True)

    birthday = models.DateField('Дата рождения пациента')

    work_place = models.CharField('Место работы', max_length=150, null=True, blank=True)

    series_passport = models.IntegerField('Серия паспорта')
    numner_passport = models.IntegerField('Номер паспорта')
    issued_passport = models.CharField('Выдан', max_length=200, null=True)
    issued_date_passport = models.DateField('Дата выдачи', null=True)
    issued_code_passport = models.CharField('Код подразделения', max_length=7, default='000-000')

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

    insurance_number = models.IntegerField('Cтраховой полис', null=True)
    insurance_end_date = models.DateField('Срок действия', null=True)
    insurance_company = models.CharField('Страховая компания', max_length=150, null=True)

    medical_record_number = models.CharField('Номер медицинской карты', max_length=100)
    date_created_medical_record = models.DateField('Дата выдачи медицинской карты пациента') 

    personal_data_doc = models.FileField('Согласие на обработку персональных данных', upload_to='pacients/docs/personal_data/%Y/%m/%d/%H-%M-%S/', null=True)
    contract_doc = models.FileField('Договор на оказание медицинских услуг', upload_to='pacients/docs/contract/%Y/%m/%d/%H-%M-%S/', null=True)

    class Meta:

        verbose_name = 'пациент'
        verbose_name_plural = "Пациенты"
    
    def __str__(self):
        return f'{self.id} | {self.last_name} {self.first_name[0].upper()}. {self.last_name[0].upper()}. '
    

class TherapeuticAndDiagnosticEvents(models.Model):
    pacient = models.ForeignKey(Pacients, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.PROTECT)

    created_date = models.DateTimeField('Дата и время создания записи', auto_now_add=True)
    started_date = models.DateTimeField('Дата и время приема')
    ended_date = models.DateTimeField('Дата и время окончания приема', null=True, blank=True)

    type = models.CharField('Тип мероприятия', choices=(
        ('лабораторное исследование', 'Лабораторное исследование'),
        ('инструментальная диагностика', 'Инструментальная диагностика'),
        ('лекарственная терапия', 'Лекарственная терапия'),
        ('физиотерапия', 'Физиотерапия'),
        ('хирургическое лечение', 'Хирургическое лечение'),
        ),
        max_length=150)
    
    event_name = models.CharField('Название проведенного мероприятия', max_length=200)
    event_result = models.TextField('Результаты мероприятия')
    
    diagnos = models.CharField('Диагнос', max_length=150)

    recomendations = models.TextField('Рекомендации по дальнейшему лечению или контрольным исследованиям')

    class Meta:
        verbose_name = 'лечебно-диагностическое  мероприятие'
        verbose_name_plural = "Лечебно-диагностические  мероприятия"

    def __str__(self) -> str:
        return f'{self.pacient.id} | {self.doctor.id} | {self.created_date}'
