from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nim = models.CharField(max_length=10, default='')
    nama_lengkap = models.CharField(max_length=50, default='')
    kelas = models.CharField(max_length=20, default='')
    gambar_profile = models.ImageField(upload_to='users', blank=True)

    def __str__(self):
        return self.nama_lengkap
