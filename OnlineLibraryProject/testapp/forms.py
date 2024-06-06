from django import forms
from django.contrib.auth.models import User
from testapp.models import Book,Magagin,NewsPaper

class SignUpFrom(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
class MagaginForm(forms.ModelForm):
    class Meta:
        model=Magagin
        fields='__all__'
class NewsForm(forms.ModelForm):
    class Meta:
        model=NewsPaper
        fields='__all__'



