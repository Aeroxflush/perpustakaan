from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', include('buku.urls')),
    path('anggota/', include('anggota.urls')),
    path('penerbit/', include('penerbit.urls')),
]
