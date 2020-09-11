from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('produk/', include('produk.urls')),
    path('pembeli/', include('pembeli.urls')),
    path('pengguna/', include('pengguna.urls')),
    path('transaksi/', include('transaksi.urls')),
    path('admin/', admin.site.urls),
]
