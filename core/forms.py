from django import forms
from .models import Port, System, Client, Note, Server


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']


class PortForm(forms.ModelForm):
    class Meta:
        model = Port
        fields = ['connector', 'shutdown', 'status']


class SystemForm(forms.ModelForm):
    class Meta:
        model = System
        fields = ['initials', 'name']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'link', 'port', 'system', 'version', 'status']


class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ['name', 'acomServer']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=300, required=False, widget=forms.TextInput(attrs={'placeholder': 'Cliente'}))


class UpdateForm(forms.Form):
    systemId = forms.ModelChoiceField(queryset=System.objects.all())
    date = forms.DateTimeField(label='Data', required=True)
