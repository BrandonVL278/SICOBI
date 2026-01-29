from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    # book
    path('book/', views.book_record, name='library_record'),
    path('book/create/', views.book_form, name='book_create'),
    path('book/<int:id>/update/', views.book_form, name='book_update'),
    path('ajax/load-subareas/', views.load_subareas, name='ajax_load_subareas'),

    # movie
    path('movies/', views.movies_record, name='movie_record'),
    path('movie/create/', views.movie_form, name='movie_create'),
    path('movie/<int:id>/update/', views.movie_form, name='movie_update'),

    # media
    path('multimedia/', views.multimedia_record, name='multimedia_record'),
    path('multimedia/create/', views.multimedia_form, name='multimedia_create'),
    path('multimedia/<int:id>/update/', views.multimedia_form, name='multimedia_update'),

    # equipment
    path('equipment/', views.equipment_record, name='equipment_record'),
    path('equipment/create/', views.equipment_form, name='equipment_create'),
    path('equipment/<int:id>/update/', views.equipment_form, name='equipment_update'),
    
    # area
    path('area/', views.area_record, name='area_record'),
    path('area/create/', views.area_form, name='area_create'),
    path('area/<int:id>/update/', views.area_form, name='area_update'),
    path('area/<int:id>/consult/', views.area_consult, name='area_consult'),

    # subarea
    path('subarea/<int:area_id>/create/', views.subarea_form, name='subarea_create'),
    path('subarea/<int:area_id>/<int:id>/update/', views.subarea_form, name='subarea_update'),
]

