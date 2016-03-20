from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

from .forms import FrancisForm

# Create your views here.
def new_francis_form(request):
    if request.method == 'POST':
        form = FrancisForm(request.POST)
        if form.is_valid():
            formulario = form.save()
            formulario.save()
            template = loader.get_template('respuesta.html')
            context = { }
            return HttpResponse(template.render(context, request))
            #return HttpResponseRedirect("/respuesta/")
    else:
        form = FrancisForm()

    template = loader.get_template('new_francis_form.html')
    context = {
        'form':form
    }
    return HttpResponse(template.render(context, request))

def respuesta_form(request):
    template = loader.get_template('respuesta.html')
    context = { }
    return HttpResponse(template.render(context, request))

