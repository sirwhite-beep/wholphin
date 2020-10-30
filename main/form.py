from django import forms
from .models import Comment


class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'phone_number', 'email', 'comment']



