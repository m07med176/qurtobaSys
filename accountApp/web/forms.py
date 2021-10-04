from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accountApp.models import Account

class RegistrationFrom(UserCreationForm):
        email = forms.EmailField(max_length = 60,help_text = "Required add a valid Email")

        class Meta:
            model = Account
            fields = ('email','username','password1','password2')

class AccountLoginForm(forms.ModelForm):
    password = forms.CharField(label="Password",
    widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields= ('email','password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email = email,password = password):
                raise forms.ValidationError("Invalid Login")

class AccountUpdate(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email','username')
    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError(f"email {email} is already in use ")
        
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError(f"username {username} is already in use ")