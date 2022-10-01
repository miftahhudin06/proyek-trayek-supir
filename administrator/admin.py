from django.contrib import admin

from administrator.models import Jenis_Angkutan, Profil, Supir


# Register your models here.
admin.site.register(Profil)
admin.site.register(Supir)
admin.site.register(Jenis_Angkutan)
