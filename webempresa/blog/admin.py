from django.contrib import admin
from .models import Category, Post

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')  # nos agregaría a la lista que se muestra en admin, el título, el autor y cuándo fue publicado
    ordering = ('author', 'published')  # cambia el orden de la búsqueda para que sean varios las categorías a buscar
    search_fields = ('title', 'content', 'author__username', 'categories__name')  # Sale una casilla de búsqueda para buscar por título, contenido y para autor usamos __username para que busque por User, para categories agregamos __name para que busque busque por la categoría name de manytomany
    date_hierarchy = 'published'  # Muestra una gerarquía según publicado
    list_filter = ('author__username', )  # Muestra del lado derecho un cuadro con todos los autores para filtrar el contenido

# Creamos un método para mostrar las categorías que no podemos mostrar ya que son un manytomany y no se puede poner en la barra

    def post_categories(self, obj):  # generamos las categorías en la barra
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])  # retorna el nombre de c por c en todas las categorias dentro de objeto ordenadas por nombre
    post_categories.short_description = "Categorías"   # Cambia el nombre que se muestra en la barra a español


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
