from .models import Response
from django.forms import ModelForm
from django import forms
class ResponseForm(forms.ModelForm):
	class Meta:
		model= Response
		fields ='__all__'
