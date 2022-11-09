from modeltranslation.translator import register, TranslationOptions
from .models import Course

@register(Course)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'language', 'direction', 'certification', 'skill', 'start_month', 'end_month',)