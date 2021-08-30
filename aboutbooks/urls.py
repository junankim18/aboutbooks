from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .models import *
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('perword', perword, name='perword'),
    path('persilent', persilent, name='persilent'),
    path('subsilent', subsilent, name='subsilent'),
    path('test', test, name='test'),
    path('brand', brand, name='brand'),
]
