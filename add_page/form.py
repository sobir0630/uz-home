from django import forms
from .models import Annoncements


class AnnoncementsForm(forms.ModelForm):

    class Meta:
        model = Annoncements
        fields = [
            'name',
            'price',
            'location',
            'description',
            'seller_contact',
            'telegram',
            'category',
            'status',
            'image',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': "E'lon nomi"
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': "Narxi"
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': "Manzil"
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control mb-2 text-secondary',
                'placeholder': "Qisqacha ma'lumot"
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control mb-2'
            }),
            'seller_contact': forms.NumberInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': "Kontaktingiz"
            }),
            'telegram': forms.TextInput(attrs={
                'class': 'form-control mb-2 text-secondary',
                'placeholder': "Telegram username (@username)"
            }),
            'category': forms.Select(attrs={
                'class': 'form-control mb-2'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control mb-2'
            }),
        }

    def clean_telegram(self):
        telegram = self.cleaned_data.get('telegram')

        # Agar foydalanuvchi umuman kiritmasa
        if not telegram:
            raise forms.ValidationError("Telegram username kiritish majburiy")

        # Agar @ bilan boshlanmasa
        if not telegram.startswith('@'):
            raise forms.ValidationError("Telegram @ bilan boshlanishi kerak")

        return telegram
