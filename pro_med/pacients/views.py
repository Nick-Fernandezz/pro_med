from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import *

# Create your views here.

@login_required
def add_pacients(request):
    if request.method == "POST":
        try:
            pacient = Pacients.objects.get(series_passport=request.POST.get('series_passport'), numner_passport=request.POST.get('numner_passport'))
            print(pacient)
            return render(request, 'pacients/add_pacient/add_pacient.html', context={
                'error': 'Пациент уже существует в базе'
            })
        except Pacients.DoesNotExist:
            pacient = Pacients.objects.create(
                avatar=request.FILES.get('avatar', None),
                first_name=request.POST.get('first_name', None),
                last_name=request.POST.get('last_name', None),
                middle_name=request.POST.get('middle_name', None),
                birthday=request.POST.get('birthday', None),
                work_place=request.POST.get('work_place', None),
                series_passport=request.POST.get('series_passport', None),
                numner_passport=request.POST.get('numner_passport', None),
                sex=request.POST.get('sex', None),
                country=request.POST.get('country', None),
                state=request.POST.get('state', None),
                city=request.POST.get('city', None),
                street=request.POST.get('street', None),
                house=request.POST.get('house', None),
                entrance=request.POST.get('entrance', None),
                apartment=request.POST.get('apartment', None),
                phone_number=request.POST.get('phone_number', None),
                email=request.POST.get('email', None),
                insurance_number=request.POST.get('insurance_number', None),
                insurance_end_date=request.POST.get('insurance_end_date', None),
                insurance_company=request.POST.get('insurance_company', None),
                date_created_medical_record=now()
            )
            
            pacient.medical_record_number = pacient.id
            pacient.save()
            return redirect('index_page')
    else:

        return render(request, 'pacients/add_pacient/add_pacient.html')
