from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.index, name=''),
    path('showparticipants', views.showparticipants, name='showparticipants'),
    path('addparticipants', views.addparticipants, name='addparticipants'),
    path('showlessons', views.showlessons, name='showlessons'),
    path('pricing', views.pricing, name='pricing'),
    # path('addparticipant', views.addparticipant,name='addparticipant'),
    path('addsup', views.addsup, name='addsup'),
    path('addsup/<int:id>', views.addsup, name='addsup'),
    path('showemployee', views.showemployee, name='showemployee'),
    path('showmhisto/<int:id>', views.showmhisto, name='showmhisto'),
    path('search', views.search, name='search'),
]
