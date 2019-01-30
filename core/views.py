from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from core.models import *


def home(request):

    return render(request, 'base.html')


def login(request):
    if request.method == 'POST':
        login = request.POST.get('user')
        senha = request.POST.get('password')
        if logar(request, user, senha):
            return redirect('/listar_cadastro')
        else:
            return redirect('listar_cadastro')
    return render(request, 'login.html')

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        login = request.POST.get('user')
        senha = request.POST.get('password')
        genero = request.POST.get('gender')
        data_nasc = request.POST.get('data_nasc')
        return redirect('/')

    return render(request, 'base_form.html')

def listar_cadastro(request):
    return render(request, 'base_lista.html')