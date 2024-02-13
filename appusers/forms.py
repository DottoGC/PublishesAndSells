from django import forms
from appusers.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from betterforms.multiform import MultiModelForm
import random

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields = [
            'telephone',
            'gender',
            'date_of_birth',
            'address',
        ]
        labels = {
            'telephone': 'Telefono',
            'gender': 'Genero',
            'date_of_birth': 'Fecha Nacimiento',
            'address': 'Direccion',
        }


class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'first_name',
				'last_name',
				'email',
                'username',
			]
		labels = {
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
                'email': 'Email',
                'username': 'Username',
		}

class CustomerMultiForm(MultiModelForm):
    form_classes = {
        'user': UserForm,
        'profile': UserProfileForm,

    }

    def save(self,commit=True):
        objects = super(CustomerMultiForm,self).save(commit=False)
        if commit:
            user=objects['user']
            user.is_active=False
            user.save()

            profile = objects['profile']
            profile.id_user = user
            classcustomer = random.randint(1, 5)
            if classcustomer==1:
                profile.class_customer='A'
                profile.available_credit=20000.00
                profile.gain_obtained=0
            elif classcustomer==2:
                profile.class_customer='B'
                profile.available_credit=15000.00
                profile.gain_obtained = 0
            elif classcustomer==3:
                profile.class_customer='C'
                profile.available_credit=10000.00
                profile.gain_obtained = 0
            elif classcustomer==4:
                profile.class_customer='D'
                profile.available_credit=5000.00
                profile.gain_obtained = 0
            elif classcustomer==5:
                profile.class_customer='E'
                profile.available_credit=1000.00
                profile.gain_obtained = 0

            profile.save()
        return objects