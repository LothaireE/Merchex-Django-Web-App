from django.contrib import admin
from listings.models import Band
from listings.models import Offer

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'genre', 'year_formed') # liste les champs que nous voulons sur l'affichage de la liste


class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'band', 'offer_type')

admin.site.register(Band, BandAdmin)
admin.site.register(Offer, OfferAdmin)
# Register your models here.

#  [X] 0008_rename_type_offer_offer_type
#  [X] 0009_band_like_new
# offers