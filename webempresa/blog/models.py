from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)  # Esta fecha será colocada manualmente y usamos from django.utils import timezone para agregarle una hora por defecto con el método now
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)  # la imagen no sería obligatoria
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)  # aquí usamos el parámetro User que nos permitirá anclarlo a un usuario que existirá en nuestra página, y luego on_delete=models.CASCADE para que se borre la entrada si se elimina el usuario / si colocamos el models.PROTECT deberíamos también agregar null y blank
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]

    def __str__(self):
        return self.title
