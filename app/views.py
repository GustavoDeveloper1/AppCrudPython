from django.shortcuts import redirect, render
from app.form import ClientesForm
from app.models import Clientes

# Create your views here.


def home(request):
    data = {}
    data['db'] = Clientes.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = ClientesForm()
    return render(request, 'formulario.html', data)


def create(request):
    form = ClientesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    data['form'] = ClientesForm(instance=data['db'])
    return render(request, 'formulario.html', data)


def update(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    form = ClientesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Clientes.objects.get(pk=pk)
    db.delete()
    return redirect('home')
