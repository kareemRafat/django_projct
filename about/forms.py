from django import forms
from . import models

class NewUser(forms.ModelForm):
    
    class Meta:
        model = models.User
        fields = ("username","password" ,'email' , 'address' , 'tall' , 'profile','dep')
