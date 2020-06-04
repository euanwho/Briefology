from .models import Dictation
import django_filters

class DictationFilter(django_filters.FilterSet):
    class Meta:
        model = Dictation
        fields = ['title', 'difficulty',]