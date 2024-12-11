from django.db import models

class Anggota(models.Model):
    kode_anggota = models.CharField(max_length=8)
    nama_anggota = models.TextField()
    alamat_anggota = models.TextField()
    kontak_anggota = models.TextField()
    email_anggota = models.TextField()
    def __str__(self):
        return self.nama_anggota