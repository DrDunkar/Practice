from django import forms
class contact(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(label='E-mail')
    number = forms.CharField( max_length=30)
    comment = forms.CharField(max_length=30)
    