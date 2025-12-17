from django import forms
from .models import annoncements

class annoncementsForm(forms.ModelForm):  
    
    class Meta:
        model = annoncements
        fields = ['name', 'description', 'price', 'image', 'seller_contact', 'location']