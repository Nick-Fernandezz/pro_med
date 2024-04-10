import os
from docxtpl import DocxTemplate
from django.conf import settings
from pacients.models import Pacients

def generate_doc_context(doc_type:str, pacient:Pacients, request=None) -> dict:
    """
    doc_type : str <- 'personal_doc' | 'contract'

    Generate context dict from pacient model for generate documents

    """

    if doc_type == 'personal_data':


        context = {
            'id': pacient.id,
            'last_name': pacient.last_name,
            'first_name': pacient.first_name,
            'passport_serias': pacient.series_passport,
            'passport_number': pacient.numner_passport,
            'issued_date_passport': pacient.issued_date_passport,
            'issued_passport': pacient.issued_passport,
            'issued_code_passport': pacient.issued_code_passport,
            'country': pacient.country,
            'state': pacient.state,
            'city': pacient.city,
            'house': pacient.house,
            'date_created_medical_record': pacient.date_created_medical_record 
        }
        if pacient.middle_name != None:
            context['middle_name'] = pacient.middle_name
        if pacient.state != None:
            context['state'] = pacient.state
        if pacient.street != None:
            context['street'] = pacient.street
        if pacient.apartment != None:
            context['apartment'] = pacient.apartment
        
        return context
    elif doc_type == 'contract':
        context = {
            'id': pacient.id,
            'last_name': pacient.last_name,
            'first_name': pacient.first_name,
            'worker': f'{request.user.last_name} {request.user.first_name} {[i for i in [request.user.middle_name, None] if i != None]}',
            'date_created_medical_record': pacient.date_created_medical_record,
            'country': pacient.country,
            'state': pacient.state,
            'city': pacient.city,
            'house': pacient.house,
            'passport_serias': pacient.series_passport,
            'passport_number': pacient.numner_passport,
            'phone': pacient.phone_number
        }
        if pacient.middle_name != None:
            context['middle_name'] = pacient.middle_name
        if pacient.state != None:
            context['state'] = pacient.state
        if pacient.street != None:
            context['street'] = pacient.street
        if pacient.apartment != None:
            context['apartment'] = pacient.apartment
        return context


def generate_personal_data_doc(context) -> str:
    
    personal_data_doc = DocxTemplate(os.path.join(settings.BASE_DIR, 'pacients\docs_templates\personal_data.docx'))
    personal_data_doc.render(context)

    doc_personal_data_path = f'{settings.BASE_DIR}/media/pacients/docs/personal_data_templates/{context['id']}/{context['last_name']}.docx'
    try:
        os.mkdir(f'{settings.BASE_DIR}/media/pacients/docs/personal_data_templates/{context['id']}')
    except FileExistsError:
        pass
    try:
        personal_data_doc.save(doc_personal_data_path)
    except FileExistsError:
        os.remove(doc_personal_data_path)
        personal_data_doc.save(doc_personal_data_path)

    return doc_personal_data_path[doc_personal_data_path.find('/media/'):]


def generate_contract_doc(context):

    contract_doc = DocxTemplate(os.path.join(settings.BASE_DIR, 'pacients\docs_templates\contract.docx'))
    contract_doc.render(context)

    contract_path = f'{settings.BASE_DIR}/media/pacients/docs/contract_templates/{context['id']}/{context['last_name']}.docx'

    try:
        os.mkdir(f'{settings.BASE_DIR}/media/pacients/docs/contract_templates/{context['id']}')
    except FileExistsError:
        pass
    try:
        contract_doc.save(contract_path)
    except FileExistsError:
        os.remove(contract_path)
        contract_doc.save(contract_path)

    return contract_path[contract_path.find('/media/'):]