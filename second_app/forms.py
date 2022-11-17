from django import forms
from .models import User

class NewUserForm(forms.ModelForm):
    # first_name = forms.CharField(label='First Name',label_suffix=':--')
    # last_name = forms.CharField(label='Last Name',error_messages={'required': 'Please enter your name'})
    # email_id = forms.CharField(label='Email',)
    class Meta():
        model=User
        fields= '__all__'


    

    
