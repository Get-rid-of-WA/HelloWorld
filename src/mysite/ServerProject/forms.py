from django import forms
from django.forms import models
from django.forms.forms import Form
from django.forms.widgets import Textarea
from .models import ServerProject

'''
用于创建新项目的表单
'''
class newServerProjectForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        required=True
    )
    description = forms.CharField(
        max_length=3000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'row': 5,
                'placeholder': 'enter the server project description here',
            }
        )
    )
    price = forms.DecimalField(
        max_digits=5, 
        decimal_places=2,
        required=True
    )
    length = forms.IntegerField(
        required=True
    )

'''
用于搜索项目的表单
'''
class SearchRequirementForm(forms.Form):
    SearchRequirement = forms.CharField(
        max_length=30
    )


'''
用于更新项目的表单
'''
class UpdateServerProjectForm(forms.Form):
    name = forms.CharField(
        max_length=30
    )
    description = forms.CharField(
        max_length=3000,
        widget=forms.Textarea(
            attrs={
                'row': 5,
            }
        )
    )
    price = forms.DecimalField(
        max_digits=5,
        decimal_places=2
    )