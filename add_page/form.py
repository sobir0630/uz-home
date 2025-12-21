from django import forms
from .models import Annoncements

class AnnoncementsForm(forms.ModelForm):  
    
    class Meta:
        model = Annoncements
        fields = ['name', 'price', 'location', 'description', 'image', 'seller_contact', 'category', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': "E'lon nomi"}),
            'price': forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': "Narxi"}),
            'location': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': "Manzil"}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-2', 'placeholder': "Qisqacha ma'lumot"}),
            'image': forms.FileInput(attrs={'class': 'form-control mb-2'}),
            'seller_contact': forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': "Kontaktingiz"}),
            'category': forms.Select(attrs={'class': 'form-control mb-2'}),
            'status': forms.Select(attrs={'class': 'form-control mb-2'}),
            'publish': forms.DateTimeInput(attrs={'class': 'form-control mb-2', 'type': 'datetime-local'}),
            
        }