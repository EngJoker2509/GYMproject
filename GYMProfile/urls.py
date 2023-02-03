from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index,name=''),	
    path('showparticipants', views.showparticipants,name='showparticipants'),
    path('addparticipants', views.addparticipants,name='addparticipants'), 
    path('showlessons', views.showlessons,name='showlessons'),  
    path('pricing', views.pricing,name='pricing'), 
    path('addparticipant', views.addparticipant,name='addparticipant'),
    path('addemployee', views.addemployee,name='addemployee'),
    path('showemployee', views.showemployee,name='showemployee'),
    path('showmhisto', views.showmhisto,name='showmhisto'),
    
]