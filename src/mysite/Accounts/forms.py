from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    MALE = 'male'
    FEMALE = 'female'

    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    name = forms.CharField(
        max_length=30, 
        required=True,
    )
    
    email = forms.CharField(
        max_length='254',
        required=True,
        widget=forms.EmailInput(),
    )

    sex = forms.CharField(
        max_length=10,
        required=True,
    )

    phone = forms.CharField(
        max_length=20,
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class newProviderForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        required=True,
    )

    email = forms.CharField(
        max_length='254',
        required=True,
        widget=forms.EmailInput(),
    )

    phone = forms.CharField(
        max_length=20,
        required=True,
    )