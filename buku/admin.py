from django.contrib import admin
from .models import Book

@admin.register(Book)
class BukuAdmin(admin.ModelAdmin):
    list_display = ('kode_buku', 'judul_buku', 'pengarang', 'penerbit', 'tahun')
    search_fields = ('judul_buku', 'pengarang', 'penerbit', 'tahun')
    list_filter = ('judul_buku', 'pengarang', 'penerbit', 'tahun')
