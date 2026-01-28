from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
     # post views 
     path('sign_in/', views.sign_in, name='sign_in'),
]
