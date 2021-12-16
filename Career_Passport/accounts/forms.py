from django import forms
from django.contrib.auth.forms import (AuthenticationForm,ReadOnlyPasswordHashField)
 
from .models import CustomUser

"""from django.contrib.auth.forms import (UserCreationForm as BaseUserCreationForm,
    UserChangeForm as BaseUserChangeForm,
)"""

"""class UserCreationForm(BaseUserCreationForm.Meta):
    class Meta(BaseUserCreationForm):
        model=CustomUser

class UserChangeForm(BaseUserChangeForm.Meta):
    class Meta(BaseUserChangeForm):
        model=CustomUser"""
 
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('user_ID','name','school_ID','student_year','student_class')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('user_ID', 'password','name','school_ID','student_year','student_class',
                  'is_active','is_admin')

    def clean_password(self):
        return self.initial["password"]