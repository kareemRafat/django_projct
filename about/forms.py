from django import forms
from . import models

class NewUser(forms.ModelForm):
    
    class Meta:
        model = models.User
        fields = ("username","password" ,'email' , 'address' , 'tall' , 'profile','dep')

    # this function will be used for the validation
    def clean(self):
 
        # data from the form is fetched using super function
        super(NewUser, self).clean()
         
        # extract the username and text field from the data
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
 
        # conditions to be met for the username length
        if len(username) > 5:
            self._errors['username'] = self.error_class([
                'Minimum 5 characters required'])
        if len(password) < 10:
            self._errors['password'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])
 
        # return any errors if found
        return self.cleaned_data