from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from administrator.models import Jenis_Angkutan, Profil, Supir

# sign up form


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

# sign in form


class SigninForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class UpdateProfilForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profil
        fields = ['avatar', 'bio']


class SupirForm(forms.ModelForm):
    nik = forms.CharField(max_length=100,
                          required=True,
                          widget=forms.TextInput(attrs={'placeholder': 'Masukan Nik',
                                                        'class': 'form-control',
                                                        }))
    nama = forms.CharField(max_length=100,
                           required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Masukan Nama',
                                                         'class': 'form-control',
                                                         }))
    tgl_lahir = forms.DateField(required=True,
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'
                                                              }))

    jadwal = forms.CharField(max_length=100,
                             required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Masukan Jadwal',
                                                           'class': 'form-control',
                                                           }))

    alamat = forms.CharField(max_length=100,
                             required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Masukan Alamat',
                                                           'class': 'form-control',
                                                           }))

    avatar = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control-file'}))

    class Meta:
        model = Supir
        fields = '__all__'


class InputAngkutan(forms.ModelForm):
    nama = forms.CharField(max_length=100,
                           required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         }))
    no_angkutan = forms.CharField(max_length=100,
                                  required=True,
                                  widget=forms.TextInput(attrs={'placeholder': 'Masukan No Angkutan',
                                                         'class': 'form-control',
                                                                }))

    rute = forms.CharField(max_length=100,
                           required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Masukan Rute',
                                                         'class': 'form-control',
                                                         }))

    class Meta:
        model = Jenis_Angkutan
        fields = '__all__'
