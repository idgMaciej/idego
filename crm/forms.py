from django import forms
from .models import Company
from django.contrib.auth.models import User


class CreateCompany(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name',)


# class RemoveUser(forms.ModelForm):
#
#     class Meta:
#         model = User
#         fields = ('username',)

class RemoveUser(forms.Form):
    username = forms.CharField(max_length=150)
