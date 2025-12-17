from django import forms
from .models import User
from django.contrib.auth.hashers import make_password


class UserSave(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def cleaned(self):
        cliened_data = super().clean()
        password = cliened_data.get("password")
        password2 = cliened_data.get("password2")
        
        if password and password2 and password != password2:
            raise forms.ValidationError("Password do not match")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # parolni hash qilamiz
        if commit:
            user.save()
        return user

