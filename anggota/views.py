from django.shortcuts import render
from .models import Anggota

def index(request):
    anggota = Anggota.objects.all()
    context = {
        'Title':'Perpustakaan STMIK Pontianak',
        'Heading':'Daftar Nama Anggota',
        'Anggota': anggota,
    }
    return render(request, "anggota.html", context)
