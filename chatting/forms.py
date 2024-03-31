from django import forms
class LoginForm(forms.Form):
    mobile_number = forms.CharField(max_length=15)

class Adminlogin(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30)
    