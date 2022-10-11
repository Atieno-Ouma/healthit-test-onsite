from django import forms
from django.forms import fields
from .models import User,Friends
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

class Adduser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'username', 'location', 'gender', 'DOB']
        widgets = {
            'DOB': DatePickerInput(),
        }

class FriendsSearchForm(forms.ModelForm):
    class Meta:
        model = Friends
        fields = ['id', 'client_name']

        # Custom form validation