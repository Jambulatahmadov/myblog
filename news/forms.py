from .models import MyNews
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class MyNewsForm(ModelForm):
    class Meta:
        model = MyNews
        fields = ['title', 'anons', 'context', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'News name'

            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'News anons'

            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Created date'

            }),
            "context": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'News Content'

            }),
        }