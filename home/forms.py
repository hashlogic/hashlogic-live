from django import forms
from .models import Contacts


class NewMessageForm(forms.ModelForm):

	class Meta:
		model = Contacts
		fields = ['name','email','subject','message']

