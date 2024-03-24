from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('addpacient/', add_pacients, name='add_pacient_page'),
    path('search/', search_pacient, name='search_pacient_page'),
    path('view/<int:pacient_id>/', pacient_detail_page, name='pacient_detail_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

