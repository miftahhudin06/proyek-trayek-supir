from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (200, 200)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    def __str__(self):
        return self.user.username


class Supir(models.Model):
    nik = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    tgl_lahir = models.DateField()
    jadwal = models.CharField(max_length=100)
    alamat = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='supir_img')

    def __str__(self):
        return self.nama


class Jenis_Angkutan(models.Model):
    no_angkutan = models.CharField(max_length=10)
    rute = models.CharField(max_length=200)

    def __str__(self):
        return self.no_angkutan


class Laporan_Narik(models.Model):
    nama = models.OneToOneField(Supir, on_delete=models.CASCADE)
    no_angkutan = models.OneToOneField(
        Jenis_Angkutan, on_delete=models.CASCADE)
    tgl = models.DateField(null=True)
    km_sebelum = models.PositiveIntegerField(default=0)
    km_sesudah = models.PositiveIntegerField(default=0)
    bbm = models.PositiveIntegerField(default=1500000)
    setoran = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nama.nama
