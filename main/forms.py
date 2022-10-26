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
            'email': 'E-mail',
            'course': 'Курс',
            'comment': 'Коментар',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'cons__input', 'placeholder': "Ім'я"}),
            'last_name': forms.TextInput(attrs={'class': 'cons__input', 'placeholder': 'Прізвище'}),
            'phone': forms.TextInput(attrs={'class': 'cons__input', 'placeholder':'Телефон'}),
            'email': forms.EmailInput(attrs={'class': 'cons__input', 'placeholder': 'Email'}),
            'course': forms.Select(attrs={'class': 'cons__input'}),
            'comment': forms.Textarea(attrs={'class': 'cons__input'})
        }
class ConsForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('first_name', 'last_name', 'phone', 'email')
        labels = {
            'first_name': "Ім'я",
            'last_name': 'Прізвище',
            'phone': 'Телефон',
            'email': 'E-mail',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'cons__input', 'placeholder': "Ім'я"}),
            'last_name': forms.TextInput(attrs={'class': 'cons__input', 'placeholder': 'Прізвище'}),
            'phone': forms.TextInput(attrs={'class': 'cons__input', 'placeholder':'Телефон'}),
            'email': forms.EmailInput(attrs={'class': 'cons__input', 'placeholder': 'Email'}),
            }