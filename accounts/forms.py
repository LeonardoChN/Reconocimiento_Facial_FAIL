from django import forms
from .models import Worker

class WorkerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['rut', 'name', 'email']
