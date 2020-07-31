from django import forms
from .models import Port, System, Client


class PortForm(forms.ModelForm):
    class Meta:
        model = Port
        fields = ['connector', 'shutdown']


class SystemForm(forms.ModelForm):
    class Meta:
        model = System
        fields = ['initials', 'name']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'link', 'port', 'system', 'version', 'status']
