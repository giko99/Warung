from django.shortcuts import render,redirect
from pengguna.forms import penggunaForm
from pengguna.models import Pengguna

# crud pengguna

def usr(request):
    if request.method == "POST":
        form = penggunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pengguna')
        else:
            print (form.errors)
    else:
        form = penggunaForm()
    return render(request,'index_pengguna.html',{
        'form':form
    })
def show_pengguna(request):
    datas = Pengguna.objects.all()
    return render(request, "show_pengguna.html", {
        'datas': datas
    })
def edit_pengguna(request, id):
    data = Pengguna.objects.get(id=id)
    form = penggunaForm(None,instance=data)
    if request.method == "POST":
        form = penggunaForm(request.POST, instance = data)
        if form.is_valid():  
            form.save()  
            return redirect('/pengguna')
    return render(request, 'edit_pengguna.html',{
        'form':form,
        'data':data,
    })  
def hapus(request, id):
    data = Pengguna.objects.get(id=id)
    data.delete()
    return redirect("/pengguna")