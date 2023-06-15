from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category")  # el campo <category_id> será dinámico, aunque ésto pasa como cadena de caracteres, lo cual no queremos así que le agregamos int: delante
]
