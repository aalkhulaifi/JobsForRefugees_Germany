from django import forms 
from .models import Category, Area


class TaskerSearch(forms.Form):
    categories = forms.ModelChoiceField(
        queryset = Category.objects.all()
        )
    areas = forms.ModelChoiceField(
        queryset = Area.objects.all()
        )