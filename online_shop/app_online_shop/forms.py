from django import forms
from .models import OnlineShop 
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class Advertisementform(ModelForm):
    class Meta:
        model = OnlineShop
        fields = ['title','description','price','auction','image','user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols':80,'rows':10}),
            'price': forms.NumberInput(attrs={'class': 'form-input'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-input'}),
            'image': forms.FileInput(attrs={'class': 'form-input'}),
    }
    def clean_title(self):
        title = self. title = self.cleaned_data['title']
        if title == '?':
            raise ValidationError('Заголовок не может начинаться с вопросительного знака')
 
        return title


    # title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class':'form-control form-control-mg'}))
    # description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-mg'}))
    # price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control form-control-mg'}))
    # auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),required=False)
    # image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control form-control-mg'}))
