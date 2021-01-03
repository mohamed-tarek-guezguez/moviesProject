import django_filters
from .models import Film

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Film
        fields = {
            'Genre': ['contains',],
        }
