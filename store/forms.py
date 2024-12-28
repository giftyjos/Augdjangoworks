from  django import forms

class Bookform(forms.Form):

    title=forms.CharField()

    author=forms.CharField()

    price=forms.IntegerField()

    language=forms.CharField()

    genre=forms.CharField()
    
    year=forms.CharField()
    