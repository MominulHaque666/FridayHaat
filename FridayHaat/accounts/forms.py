from django import forms
from django.contrib.auth import get_user_model

user = get_user_model()

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
	username = forms.CharField()
	email    = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = user.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username Is Already Taken")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = user.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("Email Is Already Taken")
		return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if confirm_password != password:
			raise forms.ValidationError("Password Did Not Match")
		return data