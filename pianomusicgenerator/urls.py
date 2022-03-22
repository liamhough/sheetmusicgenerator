from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path(r'composition/', views.composition, name='composition'),
    path(r'recording', views.recording, name='recording'),
    path(r'input_id', views.input_id, name='input_id')
]
