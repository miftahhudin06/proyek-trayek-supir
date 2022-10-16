from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import SigninForm
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin.as_view(redirect_authenticated_user=True, template_name='signin.html',
                                         authentication_form=SigninForm), name='signin'),
    path('signup/', views.signup.as_view(), name='signup'),
    path('signout/', auth_views.LogoutView.as_view(template_name='signout.html'), name='signout'),
    path('profil/', views.profil, name='profil'),
    path('datasupir/', views.data_supir, name='datasupir'),
    path('inputsupir/', views.input_supir, name='inputsupir'),
    path('profilsupir/<int:id>/', views.profil_supir, name='profilsupir'),
    path('jenisangkutan/', views.jenis_angkutan, name='jenisangkutan'),
    path('inputjenisangkutan/', views.input_jenis_angkutan,
         name='inputjenisangkutan'),
    path('editjenisangkutan/<int:id>/',
         views.edit_jenis_angkutan, name='editjenisangkutan'),
    path('laporanhasilnarik/', views.laporan_hasil_narik, name='laporanhasilnarik'),
    path('laporanbulanan/', views.laporan_bulanan, name='laporanbulanan'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
