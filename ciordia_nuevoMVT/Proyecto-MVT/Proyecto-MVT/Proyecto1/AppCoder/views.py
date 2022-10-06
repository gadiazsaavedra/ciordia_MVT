# from re import template
from AppCoder.models import Familia
from django.http import HttpResponse
from django.template import loader

# from django.shortcuts import render


# Create your views here.


def crear_familiar(request) -> HttpResponse:

    template = loader.get_template("template1.html")

    flia = Familia(nombre="Paula", parentezco="Sobrina", edad="15")
    flia_2 = Familia(nombre="Sofia", parentezco="prima", edad="20")
    flia_3 = Familia(nombre="Florencia", parentezco="ahijada", edad="29")
    flia.save()
    flia_2.save()
    flia_3.save()

    dict_de_contexto = {
        "flia": flia,
        "flia_2": flia_2,
        "flia_3": flia_3,
    }

    res = template.render(dict_de_contexto)

    return HttpResponse(res)
