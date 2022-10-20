from django.contrib import admin

from administrator.models import Jenis_Angkutan, Laporan_Narik, Profil, Supir


# Register your models here.
admin.site.register(Profil)
admin.site.register(Supir)
admin.site.register(Jenis_Angkutan)
admin.site.register(Laporan_Narik)
