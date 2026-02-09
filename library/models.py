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
    title = models.CharField(verbose_name='Título', max_length=200)

class Multimedia(models.Model):
    MULTIMEDIA_TYPES = [
        ('thesis', 'Tesis'),
        ('audiobook', 'Audiolibro'),
        ('movie', 'Película'), 
        ('documentary', 'Documental'),
        ('not specified', 'Sin especificar'),
    ]
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

    img = models.ImageField(verbose_name='Portada', upload_to='movie_covers/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])], null=True, blank=True) 
    multimedia_type = models.CharField(verbose_name='Tipo de multimedia', choices=MULTIMEDIA_TYPES, default='not specified')
    multimedia_format = models.CharField(verbose_name='Formato de multimedia', choices=FORMATS, default='dvd')
    gender = models.CharField(verbose_name='Género Cinematográfico', choices=GENDERS, default='none')
    key = models.CharField(verbose_name='Clave', max_length=20, unique=True)
    title = models.CharField(verbose_name='Título', max_length=200)
    actors = models.CharField(verbose_name='Actores', max_length=300, blank=True, null=True)
    production_company = models.CharField(verbose_name='Compañía productora', max_length=150)
    copies = models.PositiveIntegerField(verbose_name='Número de copias')
    synthesis = models.CharField(verbose_name='Sinopsis', max_length=500)
    income_date = models.DateTimeField(verbose_name='Fecha de ingreso', auto_now_add=True)


    class Meta:
        verbose_name = 'Multimedia'
        verbose_name_plural = 'Multimedias'

class Equipment(models.Model):
    DEVICE_TYPES = [
        ('laptop', 'Laptop'),
        ('desktop', 'Computadora de escritorio'),
        ('tablet', 'Tablet'),
        ('mobile', 'Dispositivo móvil'),
        ('projector', 'Proyector'),
    ]
    img = models.ImageField(verbose_name='Imagen del Equipo', upload_to='equipment_images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])], null=True, blank=True)
    key = models.CharField(verbose_name='Clave', max_length=20, unique=True)
    name = models.CharField(verbose_name='Nombre del equipo', max_length=100)
    brand = models.CharField(verbose_name='Marca', max_length=100)
    device_type = models.CharField(verbose_name='Tipo de dispositivo', choices=DEVICE_TYPES, max_length=30, default='laptop')
    details = models.CharField(verbose_name='Detalles', max_length=300)
    income_date = models.DateField(verbose_name='Fecha de ingreso', auto_now_add=True)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

class Loan(models.Model):
    TYPES = [
        ('student', 'Alumno'),
        ('teacher', 'Docente'),
        ('staff', 'Personal administrativo'),
    ]

    
    person_type = models.CharField(verbose_name='Tipo de persona', choices=TYPES, max_length=10, default='student')
    person_key = models.CharField(verbose_name='Mátricula', max_length=18)
    item = models.CharField(verbose_name='Ítem prestado', max_length=100)
    estimated_return_date = models.DateField(verbose_name='Fecha estimada de devolución')
    created_at = models.DateTimeField(verbose_name='Creado el: ', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)