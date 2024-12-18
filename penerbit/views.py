from django.shortcuts import render
from .models import Penerbit

def index(request):
    penerbit = Penerbit.objects.all()
    context = {
        'Title':'Perpustakaan STMIK Pontianak', 
        'Heading':'Daftar Penerbit Ilmu Komputer',
        'Penerbit': penerbit,
    }
    return render(request, "penerbit.html" , context)