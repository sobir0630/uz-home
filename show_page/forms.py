from django import forms

class EmailSendForm(forms.Form):
    to_email = forms.EmailField(
        label="Qabul qiluvchi email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@gmail.com'
        })
    )

    subject = forms.CharField(
        label="Mavzu",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email mavzusi'
        })
    )

    message = forms.CharField(
        label="Xabar",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Xabar matni',
            'rows': 5
        })
    )



