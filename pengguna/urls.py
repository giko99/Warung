from django.contrib import admin
from django.urls import path
from pengguna import views

urlpatterns = [
    #crud pengguna
    path('admin/', admin.site.urls),
    path('usr', views.usr),
    path('', views.show_pengguna),
    path('edit_pengguna/<int:id>', views.edit_pengguna),  
    path('hapus/<int:id>', views.hapus),
    # register apps
]
