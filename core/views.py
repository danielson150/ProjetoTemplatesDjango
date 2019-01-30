from django.shortcuts import render

def home(request):

    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')

def formulario(request):
    return render(request, 'base_form.html')

def listar_cadastro(request):
    return render(request, 'base_lista.html')