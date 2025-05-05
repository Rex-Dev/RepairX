from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('usereg/',views.usereg,name='usereg'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('emplogin/',views.emplogin,name='emplogin')
]