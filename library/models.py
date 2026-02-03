from django.db import models
from account.models import User
from django.core.validators import FileExtensionValidator

class Area(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.name
    
class SubArea(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='subareas')

    class Meta:
        ordering = ['name']
        verbose_name = 'Subarea'
        verbose_name_plural = 'Subareas'

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(verbose_name='Nombre de autor', max_length=100)
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name

class Book(models.Model):

    GENDERS = [
    ('romance', 'Romance'),
    ('action', 'Acción'),
    ('adventure', 'Aventura'),
    ('fantasy', 'Fantasía'),
    ('science_fiction', 'Ciencia ficción'),
    ('horror', 'Terror'),
    ('mystery', 'Misterio'),
    ('thriller', 'Suspenso'),
    ('drama', 'Drama'),
    ('comedy', 'Comedia'),
    ('war', 'Guerra'),
    ('historical', 'Histórico'),
    ('biography', 'Biografía'),
    ('poetry', 'Poesía'),
    ('essay', 'Ensayo'),
    ('children', 'Infantil'),
    ('young_adult', 'Juvenil'),
    ('classic', 'Clásico'),
    ('crime', 'Crimen'),
    ('self_help', 'Autoayuda'),
    ('philosophy', 'Filosofía'),
    ]

    img = models.ImageField(verbose_name='Portada*', upload_to='book_covers/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])], null=True, blank=True)
    title = models.CharField(verbose_name='Titulo*', max_length=200)
    author = models.ForeignKey(Author, verbose_name='Autor*',on_delete=models.CASCADE, related_name='books')
    clue = models.CharField(verbose_name='Clave*', max_length=20, unique=True)
    isbn = models.PositiveIntegerField(verbose_name='ISBN*', unique=True)
    area = models.ForeignKey(Area, verbose_name='Área*', on_delete=models.CASCADE, related_name='books')
    subarea = models.ForeignKey(SubArea, verbose_name='Subárea*', on_delete=models.CASCADE, related_name='books')
    editorial = models.CharField(verbose_name='Editorial*', max_length=150)
    edition = models.CharField(verbose_name='Edición', max_length=100, default='Primera edición')
    edition_date = models.DateField(verbose_name='Fecha de edición', blank=True, null=True, default=None)
    edition_place = models.CharField(verbose_name='Lugar de edición', max_length=150, blank=True, null=True, default=None)
    publication_date = models.DateField(verbose_name='Fecha de publicación*')
    publication_place = models.CharField(verbose_name='Lugar de publicación*', max_length=150)
    pages = models.PositiveIntegerField(verbose_name='Número de páginas*')
    copies = models.PositiveIntegerField(verbose_name='Número de copias*')
    gender = models.CharField(verbose_name='Género Literario*', max_length=100, choices=GENDERS, default='comedy')
    synopsis = models.CharField(verbose_name='Sinopsis*', blank=True, null=True )
#cambie textfield por charfield en synopsis 
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'


class Movie(models.Model):
    GENDERS = [
        ('none', 'Sin especificar'),
        ('action', 'Acción'),
        ('adventure', 'Aventura'),
        ('animation', 'Animación'),
        ('anthology', 'Antología'),
        ('apocalyptic', 'Apocalíptico'),
        ('biography', 'Biografía'),
        ('black-comedy', 'Comedia Negra'),
        ('children', 'Infantil'),
        ('comedy', 'Comedia'),
        ('crime', 'Crimen'),
        ('cyberpunk', 'Cyberpunk'),
        ('detective', 'Detective'),
        ('documentary', 'Documental'),
        ('drama', 'Drama'),
        ('dystopian', 'Distópico'),
        ('educational', 'Educativo'),
        ('epic', 'Épico'),
        ('experimental', 'Experimental'),
        ('family', 'Familiar'),
        ('fantasy', 'Fantasía'),
        ('film-noir', 'Cine Negro'),
        ('history', 'Histórico'),
        ('horror', 'Terror'),
        ('independent', 'Independiente'),
        ('martial-arts', 'Artes Marciales'),
        ('music', 'Musical'),
        ('musical', 'Musical'),
        ('mystery', 'Misterio'),
        ('mythology', 'Mitología'),
        ('parody', 'Parodia'),
        ('philosophical', 'Filosófico'),
        ('political', 'Político'),
        ('post-apocalyptic', 'Post-apocalíptico'),
        ('psychological', 'Psicológico'),
        ('reality', 'Realidad'),
        ('romance', 'Romance'),
        ('satire', 'Sátira'),
        ('sci-fi', 'Ciencia Ficción'),
        ('short', 'Cortometraje'),
        ('slasher', 'Asesino en Serie'),
        ('space-opera', 'Ópera Espacial'),
        ('sport', 'Deportes'),
        ('steampunk', 'Steampunk'),
        ('supernatural', 'Sobrenatural'),
        ('survival', 'Supervivencia'),
        ('teen', 'Adolescente'),
        ('thriller', 'Suspense'),
        ('tragedy', 'Tragedia'),
        ('war', 'Guerra'),
        ('western', 'Oeste'),
    ]

    FORMATS = [
        ('blu-ray', 'Blu-ray'),
        ('cd', 'CD'),
        ('dvd', 'DVD'),
        ('4k', 'Ultra HD 4K'),
        ('usb', 'USB'),
    ]


    gender = models.CharField(verbose_name='Género Cinematográfico', choices=GENDERS, default='none')
    movie_format = models.CharField(verbose_name='Formato de película', choices=FORMATS, default='dvd')

    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'

class Equipment(models.Model):
    DEVICE_TYPES = [
        ('laptop', 'Laptop'),
        ('desktop', 'Computadora de escritorio'),
        ('tablet', 'Tablet'),
        ('mobile', 'Dispositivo móvil'),
    ]

    device_type = models.CharField(verbose_name='Tipo de dispositivo', choices=DEVICE_TYPES, max_length=30, default='laptop')
    brand = models.CharField(verbose_name='Marca', max_length=100)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

class Multimedia(models.Model):
    FORMATS = [
        ('cd', 'CD'),
        ('dvd', 'DVD'),
        ('usb', 'USB'),
    ]

    multimedia_format = models.CharField(verbose_name='Formato multimedia', choices=FORMATS, default='usb', max_length=5)
    publication_date = models.DateField(verbose_name='Fecha de publiación')
    producer = models.CharField(verbose_name='Productor', max_length=100)
    gender = models.CharField(verbose_name='Género', max_length=100)
    sinopsis = models.TextField(verbose_name='Sinopsis')

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Medias'

class Loan(models.Model):
    TYPES = [
        ('student', 'Alumno'),
        ('teacher', 'Docente'),
    ]

    person_type = models.CharField(verbose_name='Tipo de persona', choices=TYPES, max_length=10, default='student')
    key = models.CharField(verbose_name='Mátricula', max_length=18)
    created_at = models.DateTimeField(verbose_name='Creado el: ', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Item(models.Model):
    TYPES = [
        ('book', 'Libro'),
        ('equipment', 'Equipo'),
        ('multimedia', 'Multimedia'),
        ('movie', 'Película'),
    ]

    STATUS = [
        ('available', 'Disponible'),
        ('loaned', 'Prestado'),
        ('lost', 'Perdido'),
    ]

    obj_type = models.CharField(verbose_name='Tipo de objeto', choices=TYPES, max_length=10, blank=False, null=False)
    status = models.CharField(verbose_name='Estado', choices=STATUS, max_length=20, default='available')
    location = models.CharField(verbose_name='Ubicación', max_length=100)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, blank=True, null=True)