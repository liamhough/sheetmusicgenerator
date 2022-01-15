from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('composition', views.composition, name='composition'),
    path('recording', views.recording, name='recording'),
]
