from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('addpacient/', add_pacients, name='add_pacient_page'),
    path('search/', search_pacient, name='search_pacient_page'),
    path('view/<int:pacient_id>/upload/personal-data/', upload_personal_data_doc, name='upload_personal_data_doc'),
    path('view/<int:pacient_id>/upload/contract/', upload_contract_doc, name='upload_contract_doc'),
    path('view/<int:pacient_id>/event/create/', create_td_event, name='create_td_event'),
    path('view/<int:pacient_id>/event/<int:event_id>/detail/', detail_event, name='detail_td_event'),
    path('view/<int:pacient_id>/event/hospitalization/create/', create_hospitalization, name='create_hospitalization'),
    path('view/<int:pacient_id>/', pacient_detail_page, name='pacient_detail_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

