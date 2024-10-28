from django.shortcuts import render
from django.shortcuts import redirect
from sayayinApp.models import Sayayin
from sayayinApp.forms import FormSayayin
# Create your views here.
def index(request):
    return render(request,'index.html')
def listado(request):
    proyectos = Sayayin.objects.all()
    data = {'proyectos': proyectos}
    return render(request,'listado.html',data)

def agregar(request):
    form = FormSayayin()
    if request.method == 'POST':
        form = FormSayayin(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request,'agregar.html',data)

def actualizar(request, id):
    proyecto = Sayayin.objects.get(id = id)
    form = FormSayayin(instance=proyecto)
    if request.method == 'POST':
        form = FormSayayin(request.POST, instance = proyecto)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request,'agregar.html',data)

def eliminar(request, id):
    proyecto = Sayayin.objects.get(id = id)
    proyecto.delete()
    return redirect('/listado')