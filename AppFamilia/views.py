from django.shortcuts import render
from AppFamilia.models import Familia
from django.http import HttpResponse


def familiar1(self):
    familiar1= Familia(nombre="Tomas", apellido="Perez", edad=21, fecha_nacimiento="2001-6-13")
    familiar1.save()
    texto=f"Familiar agregado:\n --->Nombre: {familiar1.nombre} --->Apellido: {familiar1.apellido} --->Edad: {familiar1.edad} --->Fecha de nacimiento: {familiar1.fecha_nacimiento}"
    return HttpResponse(texto)

def familiar2(self):
    familiar2= Familia(nombre="Martin", apellido="Perez", edad=40, fecha_nacimiento="1982-9-22")
    familiar2.save()
    texto=f"Familiar agregado:\n --->Nombre: {familiar2.nombre} --->Apellido: {familiar2.apellido} --->Edad: {familiar2.edad}  --->Fecha de nacimiento: {familiar2.fecha_nacimiento}"
    return HttpResponse(texto)

def familiar3(self):
    familiar3= Familia(nombre="Marcos", apellido="Ruiz", edad=13, fecha_nacimiento="2009-2-11")
    familiar3.save()
    texto=f"Familiar agregado:\n --->Nombre: {familiar3.nombre}  --->Apellido: {familiar3.apellido}  --->Edad: {familiar3.edad} --->Fecha de nacimiento: {familiar3.fecha_nacimiento}"
    return HttpResponse(texto)

def familiar4(self):
    familiar4= Familia(nombre="Romina", apellido="Campero", edad=13, fecha_nacimiento="2009-2-11")
    familiar4.save()
    texto=f"Familiar agregado:\n --->Nombre: {familiar4.nombre}  --->Apellido: {familiar4.apellido}  --->Edad: {familiar4.edad} --->Fecha de nacimiento: {familiar4.fecha_nacimiento}"
    return HttpResponse(texto)






  