from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import *

urlpatterns = [
    path('', index_page, name='index_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)