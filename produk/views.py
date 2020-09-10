from django.shortcuts import render, redirect
from . import models, forms

def index(req):
    produk = models.Produk.objects.all()
    return render(req, 'produk/index.html', {
        'data': produk,
    })

def input(req):
    form_input = forms.ProdukForm()

    if req.POST:
        form_input = forms.ProdukForm(req.POST)

        if form_input.is_valid():
            form_input.save()
        return redirect('/produk')
    
    produk = models.Produk.objects.all()    
    return render(req, 'produk/input.html', {
        'data': produk,
        'form': form_input,
    })

def detail(req, id):
    produk = models.Produk.objects.filter(pk=id).first()    
    return render(req, 'produk/detail.html', {
        'data': produk,
    })

def delete(req, id):
    models.Produk.objects.filter(pk=id).delete()
    return redirect('/produk')

def update(req, id):
    if req.POST:
        produk = models.Produk.objects.filter(pk=id).update(nama=req.POST['nama'], jenis=req.POST['jenis'], stock=req.POST['stock'], harga=req.POST['harga'])
        return redirect('/produk')

    produk = models.Produk.objects.filter(pk=id).first()    
    return render(req, 'produk/update.html', {
        'data': produk,
    })