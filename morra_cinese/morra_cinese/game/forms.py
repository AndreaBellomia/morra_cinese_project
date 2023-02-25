from django import forms



class NicknameForm(forms.Form):
    username = forms.CharField(label='Nickname', max_length=30, widget=forms.TextInput(
                              attrs={
                                        'class': "input-field", 
                                        'placeholder': 'Inserisci Nickename', 
                                        'autocomplete': "off"}))