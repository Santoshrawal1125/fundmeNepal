from django import forms
from .models import User
from django.contrib.auth.hashers import make_password
import re


class UserLoginForm(forms.Form):
    email = forms.EmailField(label="Email")


class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['name', 'email', 'phone_no', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f"Enter {field_name}"
            field.widget.attrs['class'] = 'form-control'
            field.required = True

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        phone_no = cleaned_data.get('phone_no')

        if not password or not confirm_password:
            raise forms.ValidationError("Password and Confirm Password fields are required.")

        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match!")

        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")

        if not re.match(r'^[0-9]{10}$', phone_no):
            raise forms.ValidationError("Enter a valid phone number.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'phone_no')
