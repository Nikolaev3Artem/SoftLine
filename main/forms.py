from django import forms
from .models import Request, Course

class RequestForm(forms.ModelForm):
    
    class Meta:
        model = Request
        fields = ('first_name', 'last_name', 'phone', 'email', 'course', 'comment')
        labels = {
            'first_name': "Ім'я:*",
            'last_name': 'Прізвище:*',
            'phone': 'Телефон:',
            'email': 'E-mail:*',
            'course': 'Курс:*',
            'comment': 'Коментар',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'popap_name_input', 'placeholder': "Ім'я",}),
            'last_name': forms.TextInput(attrs={'class': 'popap_surname__input', 'placeholder': 'Прізвище'}),
            'phone': forms.TextInput(attrs={'class': 'popap_phone__input', 'placeholder':'012-344-5678'}),
            'email': forms.EmailInput(attrs={'class': 'popap_email__input', 'placeholder':'example@gmail.com'}),
            'course': forms.Select(attrs={'class': 'popap_course__input'}),
            'comment': forms.Textarea(attrs={'class': 'popap_comment__input','placeholder':'Залишити коментар'})
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
            'email': forms.EmailInput(attrs={'class': 'cons__input', 'placeholder': 'example@gmail.com'}),
            }