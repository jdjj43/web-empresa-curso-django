from .models import Link


def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url  # Generamos un diccionario [claves] = valores
    return ctx
