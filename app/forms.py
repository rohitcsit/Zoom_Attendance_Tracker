from django import forms

class LoginForm(forms.Form):
    id_number = forms.CharField(max_length=20, label='Enter your ID Number')
    password = forms.CharField(widget=forms.PasswordInput(), label='Enter your Password')
