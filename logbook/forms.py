from django import forms
from .models import LogBook

    
class FormLogBook(forms.ModelForm):

    class Meta:
        model = LogBook
        fields = ('user', 'date', 'aircraft', 'ident', 'from_airport', 
                'to_airport', 'start', 'stop', 'flyTime', 'duo', 'observations',
                )

        labels = {
            'user': 'Nom', 'aircraft': 'Appareil', 'from_airport': 'From',
            'to_airport': 'To', 'start':'Départ', 'stop':'Arrivée',
            'flyTime':'Temps de vol', 'duo': 'Duo', 'observations':'Observations'
            }

        widgets = {

            ## Ajoute un attribut "hidden" au champ 'user' de la form
            'user': forms.TextInput(attrs={'type': 'hidden'}),
        }