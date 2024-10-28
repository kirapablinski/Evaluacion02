from django import forms
from sayayinApp.models import Sayayin

class FormSayayin(forms.Form):
    class Meta:
        model = Sayayin
        fields = '__all__'