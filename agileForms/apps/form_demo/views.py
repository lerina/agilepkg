from django.shortcuts import render

from .models import FormDemo
from .forms import SimpleFormDemoForm, CrispyFormDemoModelForm


def formDemoIndex(request):
    return render(request, 'form_demo/index.html', {'title':'Demo for Forms'})


def showSimpleFormDemoForm(request):
    msg=""
    if request.method == 'POST':
        form = SimpleFormDemoForm(request.POST)
        if form.is_valid():
            form.save()
            msg="form Saved"
    else:
        form = SimpleFormDemoForm()
    return render(request, 'form_demo/simpleForm.html', {'form':form,"msg":msg})


def showSimpleFormDemoBootstrapUsingTemplateTagsForm(request):
    msg=""
    if request.method == 'POST':
        form = SimpleFormDemoForm(request.POST)
        if form.is_valid():
            form.save()
            msg="form Saved"
    else:
        form = SimpleFormDemoForm()
    return render(request, 'form_demo/tmplTagsForm.html', {'form':form,"title":"Using TemplateTags",'msg':msg})


def showSimpleFormDemoBootstrapUsingCrispyModelForm(request):
    msg=""
    if request.method == 'POST':
        form = CrispyFormDemoModelForm(request.POST)
        if form.is_valid():
            form.save()
            msg="form Saved"
    else:
        form = CrispyFormDemoModelForm()
    return render(request, 'form_demo/CrispyPaperModelForm.html', {'form':form,"title":"Using Crispy FormDemo ModelForm",'msg':msg})


def modalFormSkinned(request):
    msg=""
    if request.method == 'POST':
        form = SimpleFormDemoForm(request.POST)
        if form.is_valid():
            form.save()
            msg="form Saved"
    else:
        form = SimpleFormDemoForm()
    return render(request, 'form_demo/modalFormSkinned.html',{'form':form,"title":"click to see modal form",'msg':msg})

def showModalFormDemoForm(request):
    """Very draft : SimpleFormDemoForm not really used """
    msg=""
    if request.method == 'POST':
        form = SimpleFormDemoForm(request.POST)
        if form.is_valid():
            form.save()
            msg="form Saved"
    else:
        form = SimpleFormDemoForm()
    return render(request, 'form_demo/modalForm.html', {'form':form,"msg":msg})

