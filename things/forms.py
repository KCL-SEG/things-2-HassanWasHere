"""Forms of the project."""

# Create your forms here.
from django import forms

from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'description', 'quantity')
        widgets = {
            'name': forms.TextInput(),
            'description': forms.Textarea(),
            'quantity': forms.NumberInput(),
        }
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        quantity = cleaned_data.get('quantity')
        
    