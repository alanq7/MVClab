from django import forms
from .models import Movie

class PolishClearableFileInput(forms.ClearableFileInput):
    initial_text = 'Aktualny plakat'
    input_text = 'Zmień'
    clear_checkbox_label = 'Wyczyść'

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='Tytuł',
        min_length=2,
        max_length=200,
        required=True,
        error_messages={
            'required': 'Tytuł filmu jest wymagany.',
            'min_length': 'Tytuł musi mieć co najmniej 2 znaki.',
            'max_length': 'Tytuł może mieć maksymalnie 200 znaków.',
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'Wpisz tytuł filmu',
            'required': True,
            'minlength': 2,
            'maxlength': 200,
        })
    )

    director = forms.CharField(
        label='Reżyser',
        min_length=2,
        max_length=150,
        required=True,
        error_messages={
            'required': 'Reżyser jest wymagany.',
            'min_length': 'Nazwa reżysera musi mieć co najmniej 2 znaki.',
            'max_length': 'Nazwa reżysera może mieć maksymalnie 150 znaków.',
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'Wpisz imię i nazwisko reżysera',
            'required': True,
            'minlength': 2,
            'maxlength': 150,
        })
    )

    rating = forms.IntegerField(
        label='Ocena',
        min_value=1,
        max_value=10,
        required=True,
        error_messages={
            'required': 'Ocena filmu jest wymagana.',
            'min_value': 'Ocena nie może być mniejsza niż 1.',
            'max_value': 'Ocena nie może być większa niż 10.',
            'invalid': 'Ocena musi być liczbą.',
        },
        widget=forms.NumberInput(attrs={
            'placeholder': 'Podaj ocenę od 1 do 10',
            'required': True,
            'min': 1,
            'max': 10,
        })
    )

    poster = forms.ImageField(
        label='Plakat filmu',
        required=False,
        widget=PolishClearableFileInput
    )

    class Meta:
        model = Movie
        fields = ['title', 'director', 'rating', 'poster']