from django.shortcuts import render, redirect
from . import models, forms

def index(req):
    transaksi = models.Transaksi.objects.all()
    return render(req, 'transaksi/index.html', {
        'data': transaksi,
    })

def input(req):
    form_input = forms.TransaksiForm()

    if req.POST:
        form_input = forms.TransaksiForm(req.POST)

        if form_input.is_valid():
            form_input.save()
        return redirect('/transaksi')
    
    transaksi = models.Transaksi.objects.all()    
    return render(req, 'transaksi/input.html', {
        'data': transaksi,
        'form': form_input,
    })

def detail(req, id):
    transaksi = models.Transaksi.objects.filter(pk=id).first()    
    return render(req, 'transaksi/detail.html', {
        'data': transaksi,
    })

def delete(req, id):
    models.Transaksi.objects.filter(pk=id).delete()
    return redirect('/transaksi')

def update(req, id):
    if req.POST:
        transaksi = models.Transaksi.objects.filter(pk=id).update(waktu=req.POST['waktu'], jumlah=req.POST['jumlah'], ket=req.POST['ket'])
        return redirect('/transaksi')

    transaksi = models.Transaksi.objects.filter(pk=id).first()    
    return render(req, 'transaksi/update.html', {
        'data': transaksi,
    })