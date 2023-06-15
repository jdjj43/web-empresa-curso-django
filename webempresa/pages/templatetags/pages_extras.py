from django import template
from pages.models import Page

register = template.Library()  # registramos


@register.simple_tag  # agregamos un decorador que implementara una nueva funcionalidad
def get_page_list():
    pages = Page.objects.all()
    return pages
