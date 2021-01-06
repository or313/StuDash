from django import forms
from .models import Message, Category

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('user', 'text', 'date', 'categories')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name')