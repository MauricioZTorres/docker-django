from django.shortcuts import render, redirect
from .models import comidas

# Create your views here.
def mostrar_menu(request):
    menu = comidas.objects.all()
    return render(request, 'menu.html', {'menu':menu})

def guardar_platillo(request):
    comida = comidas(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    comida.save()
    return redirect('/menu/')

def eliminar_platillo(request, comida_id):
    comida = comidas.objects.get(id=comida_id)
    comida.delete()
    return redirect('/menu/')

def actualizar_platillo(request, comida_id):
    comida = comidas.objects.get(id=comida_id)

    if request.method == 'GET':
        return render(request, 'actualizar.html', {'comida':comida})
    
    elif request.method == 'POST':
        comida.name = request.POST['name']
        comida.description = request.POST['description']
        comida.price = request.POST['price']
        comida.save()
        return redirect('/menu/')
    