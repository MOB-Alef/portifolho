from django import forms

class Cometarioform(forms.Form):
    nome = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control','placehoder': 'seu nome'
            }
        )
    )
    corpo = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Deixe um comentário'}
        ),
    )