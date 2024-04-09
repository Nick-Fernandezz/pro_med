from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from doctors.models import Doctors
from django.conf import settings
from django.contrib import messages
import os

from .models import *
from .forms import *

import qrcode
from qrcode.image.svg import SvgPathImage
from docxtpl import DocxTemplate

from .scripts.doc_generator import generate_doc_context, generate_personal_data_doc, generate_contract_doc
# Create your views here.


@login_required
def search_pacient(request):
    if request.GET:
        if request.GET.get('search_type') == 'passport':
            try:
                pacient = Pacients.objects.get(series_passport=request.GET.get('series_passport', None), numner_passport=request.GET.get('numner_passport', None))
                return redirect('pacient_detail_page', pacient.id)
            except Pacients.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'Пациент не найден')
                return redirect('search_pacient_page')
            except ValueError:
                messages.add_message(request, messages.ERROR, 'Введены некорректные данные')
                return redirect('search_pacient_page')
        elif request.GET.get('search_type') == 'insurance_number':
            try:
                pacient = Pacients.objects.get(insurance_number=request.GET.get('insurance_number', None))
                return redirect('pacient_detail_page', pacient.id)
            except Pacients.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'Пациент не найден')
                return redirect('search_pacient_page')
            except ValueError:
                messages.add_message(request, messages.ERROR, 'Введены некорректные данные')
                return redirect('search_pacient_page')
        elif request.GET.get('search_type') == 'medical_record_number':
            try:
                pacient = Pacients.objects.get(medical_record_number=request.GET.get('medical_record_number', None))
                return redirect('pacient_detail_page', pacient.id)
            except Pacients.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'Пациент не найден')
                return redirect('search_pacient_page')
            except ValueError:
                messages.add_message(request, messages.ERROR, 'Введены некорректные данные')
                return redirect('search_pacient_page')
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
    
    td_events = TherapeuticAndDiagnosticEvents.objects.filter(pacient=pacient).order_by('-started_date')
    
    qr = qrcode.QRCode(image_factory=SvgPathImage)
    qr.add_data(f'http://{settings.ALLOWED_HOSTS[0]}/pacients/view/{pacient.id}/')
    qr.make(fit=True)
    
    print(len(qr.get_matrix()[0]), len(qr.get_matrix()))

    return render(request, 'pacients/pacient_detail.html', context={
        'pacient': pacient,
        'td_events': td_events,
        'qr_size': (len(qr.get_matrix()[0]), len(qr.get_matrix())),
        'qr_matrix': qr.get_matrix(),
        'personal_doc_url': generate_personal_data_doc(generate_doc_context('personal_data', pacient)),
        'contract_doc_url': generate_contract_doc(generate_doc_context('contract', pacient, request))
    })


@login_required
def upload_personal_data_doc(request, pacient_id):
    if request.method == 'POST':
        pacient = Pacients.objects.get(id=pacient_id)
        pacient.personal_data_doc = request.FILES['personal-data-doc']
        pacient.save()
        return redirect('pacient_detail_page', pacient.id)


@login_required
def upload_contract_doc(request, pacient_id):
    if request.method == "POST":
        pacient = Pacients.objects.get(id=pacient_id)
        pacient.contract_doc = request.FILES['contract-doc']
        pacient.save()
        return redirect('pacient_detail_page', pacient.id)

@login_required
def create_td_event(request, pacient_id):
    if request.method == "GET":
        pacient = get_object_or_404(Pacients, id=pacient_id)
        doctors = Doctors.objects.filter(is_active=True)
        return render(request, 'pacients/td_events/create_event.html', context={
            'pacient': pacient,
            'doctors': doctors
        })
    else:

        td_event = TherapeuticAndDiagnosticEvents.objects.create(
            pacient=get_object_or_404(Pacients, id=pacient_id),
            doctor_id=request.POST.get('doctor'),
            type=request.POST.get('type'),
            event_name=request.POST.get('event_name'),
            created_date=now(),
            started_date=request.POST.get('date'),
        )
        td_event.save()
        return redirect('pacient_detail_page', pacient_id)


@login_required
def detail_event(request, pacient_id, event_id):
    td_event = get_object_or_404(TherapeuticAndDiagnosticEvents, id=event_id, pacient__id=pacient_id)
    if request.method == 'GET':
        td_event_form = TherapeuticAndDiagnosticEventsForm(instance=td_event)
        return render(request, 'pacients/td_events/detail_event.html', context={
            'event': td_event,
            'td_event_form': td_event_form
        })
    else:
        form = TherapeuticAndDiagnosticEventsForm(request.POST, instance=td_event)
        if form.is_valid():
            form.save()
            return redirect('pacient_detail_page', pacient_id)
        

@login_required
def create_hospitalization(request, pacient_id):
    form = CreateHospitalizationForm(pacient_id)
    pacient = get_object_or_404(Pacients, id=pacient_id)
    return render(request, 'pacients/td_events/create_hospitalization.html', context={
        'form': form,
        'pacient': pacient
    })