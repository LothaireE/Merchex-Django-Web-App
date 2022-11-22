from django import forms
from listings.models import Band, Offer


class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)


class BandForm(forms.ModelForm):
   class Meta:
      model = Band
      fields = '__all__' # si je veux copier tous les champs du Model Band
      # exclude = ("official_page",) # si je veux exclure certains champs. La "," est requise.

class OfferForm(forms.ModelForm):
   class Meta:
      model = Offer
      fields = '__all__'