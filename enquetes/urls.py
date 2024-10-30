from django.urls import path 
from enquetes.views import Enquetes

urlpatterns = [
    path('', Enquetes, name='enquetes'),
]