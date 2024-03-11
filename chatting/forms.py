from django import forms
class LoginForm(forms.Form):
    mobile_number = forms.CharField(max_length=15)