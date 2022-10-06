# from multiprocessing import context
# from re import template
# from django.shortcuts import render

# import random

from AppCoder.models import Familiar
from django.http import HttpResponse

# Create your views here.
from django.template import loader


def Saludo_con_template(request) -> HttpResponse:
    template = loader.get_template("template1.html")

    familiar1 = Familiar(id=1, nombre="Profesor", apellido="Neurus", edad=30)
    familiar2 = Familiar(id=2, nombre="Hijitus", apellido="Sombreritus", edad=12)
    familiar3 = Familiar(id=3, nombre="Oaky", apellido="Cosagolda", edad=3)
    familiar1.save()
    familiar2.save()
    familiar3.save()

    context = {
        "familiar1": familiar1,
        "familiar2": familiar2,
        "familiar3": familiar3,
    }
    """
    mi_archivo = open(
        "D:\CODER\ProyectoCoder\ProyectoCoder\ProyectoCoder\templates\templates1.html"
    )
    template = Template(mi_archivo.read())
    mi_archivo.close()

    context = Context()"""

    res = template.render(context)
    return HttpResponse(res)


"""
def crear_profesor(request):
    profe= Profesor(nombre="Ricardo", apellido="Ruben", email="ric@coder.com", profesion="Tecnico electronico")
    
    return HttpResponse(f"Estoy creando un profesor: {profe.nombre} {profe.apellido}. Su profesion es: {profe.profesion}")
"""
