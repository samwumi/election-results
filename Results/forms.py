from django import forms
from .models import AnnouncedLgaResults

class PollingUnitResultForm(forms.ModelForm):
    class Meta:
        model = AnnouncedLgaResults
        fields = '__all__'  # You can specify the fields you want to display
