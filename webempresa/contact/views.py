from django.shortcuts import render, redirect
from .forms import ContactForm  # llamamos el formulario
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)  # Si hay un método post guarda los datos en el formulario
        if contact_form.is_valid():
            name = request.POST.get('name', '')  # Devuelve name sino una cadena vacia
            email = request.POST.get('email', '')  # Devuelve email sino una cadena vacia
            content = request.POST.get('content', '')  # Devuelve content sino una cadena vacia
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                f"De {name} <{email}>\n\nEscribió\n\n{content}",
                "no-contestas@inbox.mailtrap.io",
                ["jdavidox@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()  # ahora enviamos el email
                # Todo ha ido bien redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")
            # Algo no ha ido bien, redireccionamos a FAIL

    return render(request, "contact/contact.html", {'form': contact_form})
