from django.urls import path
from . import views


urlpatterns = [
    path('<int:page_id>/<slug:page_slug>', views.page, name="page")  # el campo <page_id> será dinámico, aunque ésto pasa como cadena de caracteres, lo cual no queremos así que le agregamos int: delante
]
