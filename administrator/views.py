from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required

from administrator.models import Jenis_Angkutan, Supir

from .forms import InputAngkutan, SignupForm, SigninForm, UpdateProfilForm, UpdateUserForm, SupirForm

# Create your views here.


class signup(View):
    form_class = SignupForm
    initial = {'key': 'value'}
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


class signin(LoginView):
    form_class = SigninForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # setel sesi kedaluwarsa ke 0 detik. Jadi secara otomatis akan menutup sesi setelah browser ditutup.
            self.request.session.set_expiry(0)

            # Setel sesi sebagai dimodifikasi untuk memaksa pembaruan data/cookie disimpan.
            self.request.session.modified = True

        # jika tidak, sesi browser akan berlangsung selama waktu cookie sesi "SESSION_COOKIE_AGE" yang ditentukan di settings.py
        return super(signin, self).form_valid(form)


def dispatch(self, request, *args, **kwargs):
    # akan dialihkan ke halaman beranda jika pengguna mencoba mengakses halaman daftar saat login
    if request.user.is_authenticated:
        return redirect(to='/')

    # jika tidak, proses pengiriman seperti biasanya
    return super(signup, self).dispatch(request, *args, **kwargs)


@login_required
def profil(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profil_form = UpdateProfilForm(
            request.POST, request.FILES, instance=request.user.profil)

        if user_form.is_valid() and profil_form.is_valid():
            user_form.save()
            profil_form.save()
            messages.success(request, 'Profil kamu berhasil diperbarui')
            return redirect(to='profil')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profil_form = UpdateProfilForm(instance=request.user)
    return render(request, 'profil.html', {'user_form': user_form, 'profil_form': profil_form})


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def data_supir(request):
    supir = Supir.objects.all()
    return render(request, 'data_supir.html', {'supir': supir})


@login_required
def input_supir(request):
    if request.method == 'POST':
        supir_form = SupirForm(request.POST, request.FILES)
        if supir_form.is_valid:
            try:
                supir_form.save()
                messages.success(request, 'Supir berhasil ditambahkan')
                return redirect(to='datasupir')
            except:
                pass
    else:
        supir_form = SupirForm()
    return render(request, 'input_supir.html', {'supir_form': supir_form})


@login_required
def profil_supir(request, id):
    supir1 = Supir.objects.get(id=id)
    if request.method == 'POST':
        supir_form = SupirForm(request.POST, request.FILES, instance=supir1)
        if supir_form.is_valid:
            supir_form.save()
            return redirect(to='datasupir')
    else:
        supir_form = SupirForm(instance=supir1)
    return render(request, 'profil_supir.html', {'supirform': supir_form, 'supir1': supir1})


@login_required
def jenis_angkutan(request):
    jenisAngkutan = Jenis_Angkutan.objects.all()
    return render(request, 'jenis_angkutan.html', {'jenisangkutan': jenisAngkutan})


@login_required
def input_jenis_angkutan(request):
    if request.method == 'POST':
        angkutan_form = InputAngkutan(request.POST)
        if angkutan_form.is_valid:
            angkutan_form.save()
            return redirect(to='jenisangkutan')
    else:
        angkutan_form = InputAngkutan()
    return render(request, 'form_angkutan.html', {'angkutan_form': angkutan_form})


@login_required
def edit_jenis_angkutan(request, id):
    angkutan = Jenis_Angkutan.objects.get(id=id)
    if request.method == 'POST':
        angkutan_form = InputAngkutan(request.POST, instance=angkutan)
        if angkutan_form.is_valid:
            angkutan_form.save()
            return redirect(to='jenisangkutan')
    else:
        angkutan_form = InputAngkutan(instance=angkutan)
    return render(request, 'form_angkutan.html', {'angkutan_form': angkutan_form})


@ login_required
def laporan_hasil_narik(request):
    return render(request, 'laporan_hasil_narik.html')


@ login_required
def laporan_bulanan(request):
    return render(request, 'laporan_bulanan.html')
