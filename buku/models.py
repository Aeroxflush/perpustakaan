from django.db import models

class Book(models.Model):
    kode_buku = models.CharField(max_length=8)
    judul_buku= models.TextField()
    pengarang = models.TextField()
    penerbit = models.TextField()
    tahun = models.TextField()
    def __str__(self):
        return self.judul_buku