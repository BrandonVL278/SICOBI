from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from library.models import Book, Movie, Multimedia, Equipment, Area, SubArea, Author
from library.forms import BookForm, MovieForm, MultimediaForm, EquipmentForm, AreaForm, SubAreaForm, AuthorForm
# Index
@login_required
def index(request):
    return render(request, 'index.html')
# Book
@login_required

def book_record(request):
	books = Book.objects.all()
	return render(request, 'book/record.html', {'books': books})
@login_required
def book_form(request, id=None):
	areas = Area.objects.all()

	if id:
		book = get_object_or_404(Book, id=id)
		form = BookForm(request.POST or None, instance=book)
	else:
		form = BookForm(request.POST or None)

	if request.method == 'POST' and form.is_valid():
		book_obj = form.save(commit=False)
		book_obj.save()
		return redirect('library:library_record')

	return render(request,'book/form.html', {
		'form': form,
		'areas': areas,        
	})

def load_subareas(request):
	area_id = request.GET.get('area')
	subareas = SubArea.objects.filter(area_id=area_id).order_by('name')
	return render(request, 'book/subarea_dropdown_list_options.html', {'subareas': subareas})

@login_required
def author_form(request, id=None):
	if id:
		author = get_object_or_404(Author, id=id)
		form = AuthorForm(request.POST or None, instance=author)
	else:
		form = AuthorForm(request.POST or None)

	if request.method == 'POST' and form.is_valid():
		author_obj = form.save(commit=False)
		author_obj.save()
		return redirect('library:book_create')
	return render(request, 'book/author_form.html', {
		'form':form,
	})



# Movie
@login_required
def movies_record(request):
	movies = Movie.objects.all()
	return render(request, 'movie/record.html', {'movies': movies})

@login_required
def movie_form(request, id=None):
	areas = Area.objects.all()

	if id:
		movie = get_object_or_404(Movie, id=id)
		form = MovieForm(request.POST or None, instance=movie)
	else:
		form = MovieForm(request.POST or None)

	if request.method == 'POST' and form.is_valid():
		movie_obj = form.save(commit=False)
		movie_obj.save()
		return redirect('library:movie_record')
	
	return render(request, 'movie/form.html', {
		'form': form, 
		'areas': areas,        
	})

# Media
@login_required
def multimedia_record(request):
	multimedias = Movie.objects.all()
	return render(request, 'multimedia/record.html', {'multimedias': multimedias})

@login_required
def multimedia_form(request, id=None):
	areas = Area.objects.all()

	if id:
		multimedia = get_object_or_404(Multimedia, id=id)
		form = MultimediaForm(request.POST or None, request.FILES or None, instance=multimedia)
	else:
		form = MultimediaForm(request.POST or None, request.FILES or None)

	if request.method == 'POST' and form.is_valid():
		multimedia_obj = form.save(commit=False)
		multimedia_obj.save()
		return redirect('library:multimedia_record')

	return render(request, 'multimedia/form.html', {
		'form': form,
		'areas': areas,        
	})
# Equipment
@login_required
def equipment_record(request):
	equipments = Equipment.objects.all()
	return render(request, 'equipment/record.html', {'equipment':equipments})

@login_required
def equipment_form(request, id=None):
	areas = Area.objects.all()

	if id:
		equipment = get_object_or_404(Equipment, id=id)
		form = EquipmentForm(request.POST or None, instance=equipment)
	else:
		form = EquipmentForm(request.POST or None)

	if request.method == 'POST' and form.is_valid():
		equipment_obj = form.save(commit=False)
		equipment_obj.save()
		return redirect('library:equipment_record')

	return render( request,'equipment/form.html', {
		'form': form,
		'areas': areas,        
	})

# Area
@login_required
def area_record(request):
	areas = Area.objects.all()
	return render(request, 'area/record.html', {'areas':areas})

@login_required
def area_form(request, id=None):
	if id:
		area = get_object_or_404(Area, id=id)
		form = AreaForm(request.POST or None, instance=area)
	else:
		form = AreaForm(request.POST or None)

	if request.method == 'POST' and form.is_valid():
		area_obj = form.save(commit=False)
		area_obj.save()
		return redirect('library:area_record')
	
	return render(request, 'area/form.html', {
		'form':form
	})

@login_required
def area_consult(request, id):
	area = get_object_or_404(Area, id=id)
	subareas = SubArea.objects.filter(area=area)
	return render(request, 'area/consult.html', {
		'area':area,
		'subareas':subareas,
	})

@login_required
def subarea_form(request, area_id, id=None):
    area = get_object_or_404(Area, id=area_id)

    if id:
        subarea = get_object_or_404(SubArea, id=id, area=area)
        form = SubAreaForm(request.POST or None, instance=subarea)
    else:
        form = SubAreaForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        subarea_obj = form.save(commit=False)
        subarea_obj.area = area
        subarea_obj.save()
        return redirect('library:area_consult', id=area.id)

    return render(request, 'subarea/form.html', {
        'form': form,
        'area': area,
    })