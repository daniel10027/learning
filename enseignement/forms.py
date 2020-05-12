from django import forms 




class Contact_Form(forms.Form):
    """Model definition for ContactForm."""
    nom     = forms.CharField()
    email   = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
