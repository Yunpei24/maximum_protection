from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border focus:outline-none focus:border-blue-500',
            'placeholder': 'Votre nom'
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border focus:outline-none focus:border-blue-500',
            'placeholder': 'Votre email'
        })
    )
    
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border focus:outline-none focus:border-blue-500',
            'placeholder': 'Sujet'
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border focus:outline-none focus:border-blue-500',
            'placeholder': 'Votre message',
            'rows': 6
        })
    )