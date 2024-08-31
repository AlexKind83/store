from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField(
        label = 'Имя пользователя',
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'class': 'form-control',
                                      'placeholder': 'Введите ваше имя пользователя'}))
    password = forms.CharField(
        label = 'Пароль',
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          'class': 'form-control',
                                          'placeholder': 'Введите ваш пароль'}),
    )


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )

    first_name = forms.CharField(
        label= 'Имя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя',
            }
        )
    )
    last_name = forms.CharField(
        label= 'Фамилия',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Введите вашу фамилию",
            }
        )
    )
    username = forms.CharField(
        label= 'Имя пользователя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Введите ваше имя пользователя",
            }
        )
    )
    email = forms.CharField(
        label= 'Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Введите ваш email youremail@example.com",
            }
        )
    )
    password1 = forms.CharField(
        label= 'Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Введите ваш пароль",
            }
        )
    )
    password2 = forms.CharField(
        label= 'Подтверждение пароля',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Поддвердите ваш пароль",
            }
        )
    )


class ProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'image',
            'first_name',
            'last_name',
            'username',
            'email',
        )

    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-contol mt-3'
            }
        ), required=False
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Введите ваше имя',
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите вашу фамилию',
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя пользователя',
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Введите ваш email youremail@example.com",
            }
        )
    )

