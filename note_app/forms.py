from django import forms
from .models import *


class signupform(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'


class notesForm(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'


class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'