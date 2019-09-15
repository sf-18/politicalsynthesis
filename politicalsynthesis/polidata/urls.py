from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('elections', views.elections, name='elections'),
    path('candidate_list', views.candidate_list, name='candidate_list'),
    path('<candidate_name>', views.candidate_page, name='candidate_page')
]