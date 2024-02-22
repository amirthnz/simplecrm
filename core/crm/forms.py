from django import forms
from crm import models


class AddpersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = '__all__'

class AddreasonForm(forms.ModelForm):
    class Meta:
        model = models.ReasonToVisit
        fields = '__all__'