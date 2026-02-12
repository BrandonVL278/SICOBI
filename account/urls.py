from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
     # post views 
     # login & logout
     path('sign_in/', views.sign_in, name='sign_in'),
     path('logout/', views.sign_out, name='logout'),

     # user
     path('users/', views.user_record, name='user_record'),
     path('users/create/', views.user_form, name='user_create'),
     path('users/<int:id>/update/', views.user_form, name='user_update'),
]
