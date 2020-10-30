from django import forms
from .models import Complaint, Enrol, Enroldetail


class Complaintform(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'phone', 'email', 'complaint']


class Enrolform(forms.ModelForm):
    class Meta:
        model = Enrol
        fields = '__all__'


class Enroldetailform(forms.ModelForm):
    class Meta:
        model = Enroldetail
        fields = '__all__'

