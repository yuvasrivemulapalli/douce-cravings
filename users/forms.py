from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from users.models import Details

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    #password = forms.CharField(widget=forms.PasswordInput, required=True,
    #                           min_length=5)
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), required=True, min_length=5)

    email = forms.EmailField(max_length=50, required=True)

    first_name = forms.CharField(max_length=30, required=True, validators=[
        RegexValidator(r'^[a-zA-Z]*$', message="First name should not contain numerics")])
    last_name = forms.CharField(max_length=30, required=True, validators=[
        RegexValidator(r'^[a-zA-Z]*$', message="Last name should not contain numerics")])
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], required=True)

class ProfileForm(RegistrationForm):
    ROLE_CHOICES = [('Admin', 'Admin'), ('User', 'User')]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'gender', 'role']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # Set the username field as readonly
        self.fields['username'].widget.attrs['readonly'] = True




