from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput({'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password', max_length=30, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    # Check The Email Address If Already Have Existed.
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError('This Email Already Exists!')
        return email

    # Check Password Confirm.
    def clean(self):
        clean_data = super().clean()
        p1 = clean_data.get('password1')
        p2 = clean_data.get('password2')
        if p1 and p2:
            if p1 != p2:
                raise forms.ValidationError("Password Doesn't Match!")

    # Check Username If Already Have Existed.
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError('This Username Already Exists!')
        return username
