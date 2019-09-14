from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bylocation', views.location_selection, name='location_selection'),
    path('candidate_list', views.candidate_list, name='candidate_list')
]