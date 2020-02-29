from django import forms
from .models import Notes

class NotesCreate(forms.Modelform):

    class Meta:
        model = Notes
        fields = '__all__'
