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



def view(request,pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    return render(request,'view.html',data)