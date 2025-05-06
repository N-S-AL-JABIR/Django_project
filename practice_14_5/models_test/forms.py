from django import forms
from .models import models_test

class ModelTestForm(forms.ModelForm):
    class Meta:
        model = models_test
        fields = '__all__'