from django import forms
from .models import Restaurant
from django.contrib.auth.models import User


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

        widgets = {
        	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        }

class SignupForm(forms.Modelform):
	class Meta:
	model = User
	fields = ['username', 'first_name', 'last_name','email', 'password']

	widgets={
	'password':forms.PasswordInput(),
	}

class SigninForm(forms.form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widgets=forms.PasswordInput())

	user = authenticate(username=username, password=password)

	if user is not null 
		login(request, user)
		return redirect('restaurant-list')

	context = {
		"forms" : form
	}

	return render(request, "signin.html", context)