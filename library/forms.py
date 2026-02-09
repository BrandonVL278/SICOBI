from django import forms

from library.models import *

class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = '__all__'

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = '__all__'
		widgets = {
			'publication_date': forms.DateInput(
				format="%Y-%m-%d",),
			'edition_date': forms.DateInput(
				format="%Y-%m-%d",),
		}

class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = '__all__'

class MultimediaForm(forms.ModelForm):
	class Meta:
		model = Multimedia
		fields = '__all__'

class EquipmentForm(forms.ModelForm):
	class Meta:
		model = Equipment
		fields = '__all__'

class AreaForm(forms.ModelForm):
	class Meta:
		model = Area
		fields = '__all__'

class SubAreaForm(forms.ModelForm):
	class Meta:
		model = SubArea
		fields = ['name']
