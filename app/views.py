from django.shortcuts import redirect, render
from app.form import AtletasForm
from app.models import Atleta

# Create your views here.


def home(request):
    data = {}
    data['db'] = Atleta.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = AtletasForm()
    return render(request, 'formulario.html', data)


def create(request):
    form = AtletasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Atleta.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Atleta.objects.get(pk=pk)
    data['form'] = AtletasForm(instance=data['db'])
    return render(request, 'formulario.html', data)


def update(request, pk):
    data = {}
    data['db'] = Atleta.objects.get(pk=pk)
    form = AtletasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Atleta.objects.get(pk=pk)
    db.delete()
    return redirect('home')
