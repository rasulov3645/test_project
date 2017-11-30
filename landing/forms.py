from django import forms
from .models import *

class SubcriberForm(forms.ModelForm):

    class Meta:
        model = Subcriber

        # Поля которые необходими ключить
        #fields = []

        # Поля которые необходимо исключить
        exclude = [""]
