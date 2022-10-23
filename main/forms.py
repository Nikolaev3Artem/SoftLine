from django import forms
from .models import Request, Course

class RequestForm(forms.ModelForm):
    
    class Meta:
        model = Request
        fields = ('first_name', 'last_name', 'phone', 'email', 'course', 'comment')
        labels = {
            'first_name': "Ім'я",
            'last_name': 'Прізвище',
            'phone': 'Телефон',
            'email': 'E-mai',
            'course': 'Курс',
            'comment': 'Коментар',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'name_input', 'placeholder': "Ім'я"}),
            'last_name': forms.TextInput(attrs={'class': 'name_input', 'placeholder': 'Прізвище'}),
            'phone': forms.TextInput(attrs={'class': 'phone_input', 'placeholder':'Телефон'}),
            'email': forms.EmailInput(attrs={'class': 'email_input'}),
            'comment': forms.Textarea(attrs={'class': 'comment_input'})
        }