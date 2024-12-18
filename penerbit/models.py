from django.db import models

class Penerbit(models.Model):
    kode_penerbit = models.CharField(max_length=8)
    nama_penerbit = models.TextField()
    alamat_penerbit = models.TextField()
    kota_penerbit = models.TextField()
    telp_penerbit = models.TextField()
    email_penerbit = models.TextField()
    def __str__(self):
        return self.nama_penerbit