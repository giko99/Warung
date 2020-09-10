from django.shortcuts import render, redirect
from . import models, forms

def index(req):
    pembeli = models.Pembeli.objects.all()
    return render(req, 'pembeli/index.html',{
        'data': pembeli,
    })

def input(req):
    form_input = forms.PembeliForm()
    if req.POST:
        form_input = forms.PembeliForm(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/pembeli')
    return render(req, 'pembeli/input.html',{
        'form' : form_input,
    })

def detail(req, id):
    pembeli = models.Pembeli.objects.filter(pk=id).first()
    return render(req, 'pembeli/detail.html', {
        'data': pembeli,
    })

def delete(req, id):
    models.Pembeli.objects.filter(pk=id).delete()
    return redirect('/pembeli')

def update(req, id):
    if req.POST:
        pembeli = models.Pembeli.objects.filter(pk=id).update(
            nama=req.POST['nama'], 
            alamat=req.POST['alamat'], 
            telp=req.POST['telp'])
        return redirect('/pembeli')

    pembeli = models.Pembeli.objects.filter(pk=id).first()
    return render(req, 'pembeli/update.html', {
        'data': pembeli,
    })