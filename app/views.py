from django.shortcuts import render
from app.form import ClientesForm

# Create your views here.


def home(request):
    return render(request, 'index.html')


def form(request):
    data = {}
    data['form'] = ClientesForm()
    return render(request, 'formulario.html', data)
