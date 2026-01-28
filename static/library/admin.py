from django.contrib import admin
from .models import Book, Item, Area, Loan, Equipment, Multimedia, SubArea

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'author', 'area', 'subarea')
    search_fields = ('isbn', 'title')

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(SubArea)
class SubAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'area')
    search_fields = ('name', 'area__name')

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('person_type', 'key', 'created_at', 'user')
    search_fields = ('key', 'user')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'brand')
    search_fields = ('device_type', 'brand')

@admin.register(Multimedia)
class MultimediaAdmin(admin.ModelAdmin):
    list_display = ('gender',)