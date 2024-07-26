from django import forms
from core.models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        exclude = ['added_on']