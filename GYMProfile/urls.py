from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.index, name=''),
    path('showparticipants', views.show_participants, name='showparticipants'),
    path('addparticipants', views.add_participants, name='addparticipants'),
    path('addemployee', views.add_employee, name='addemployee'),
    path('showlessons', views.show_lessons, name='showlessons'),
    path('packages', views.pricing, name='pricing'),
    path('showemployee', views.show_employee, name='showemployee'),
    path('showmhisto/<int:id>', views.show_mhisto, name='showmhisto'),
    path('userprofile/<int:id>', views.userprofile, name='userprofile'),
    path('signout', views.signout_user, name='signout'),
]
