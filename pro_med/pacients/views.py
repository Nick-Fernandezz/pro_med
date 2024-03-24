from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import *
from django.conf import settings

import qrcode
from qrcode.image.svg import SvgPathImage
# Create your views here.


@login_required
def search_pacient(request):
    return render(request, 'pacients/search/pacients.html')


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


@login_required
def pacient_detail_page(request, pacient_id):
    pacient = get_object_or_404(Pacients, id=pacient_id)
    if not pacient.medical_record_number:
        pacient.medical_record_number = f'{pacient.last_name[0].upper()}{pacient.id}'
        pacient.save()
        print(list(pacient))
    
    
    qr = qrcode.QRCode(image_factory=SvgPathImage)
    qr.add_data(f'http://{settings.ALLOWED_HOSTS[0]}/pacients/view/{pacient.id}/')
    qr.make(fit=True)
    
    print(len(qr.get_matrix()[0]), len(qr.get_matrix()))

    return render(request, 'pacients/pacient_detail.html', context={
        'pacient': pacient,
        'qr_matrix': qr.get_matrix()
    })
