from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Band(models.Model):

    class Genre(models.TextChoices):
        ROCK = 'ROCK'
        RAP = 'RAP'
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        METAL = 'METAL'

    def __str__(self) -> str:
        return f'{self.name}'


    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.TextField(null=True, blank=True)
    year_formed = models.fields.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_page = models.fields.URLField(null=True, blank=True)

class Offer(models.Model):


    class OfferType(models.TextChoices):
        RECORDS = 'RECORDS'
        CLOTHING = 'CLOTHES'
        POSTERS = 'POSTERS'
        FURNITURE = 'FURNITU'
        MISCELLANEOUS = 'MISC'

    def __str__(self) -> str:
        return f'{self.title}'


    title = models.fields.CharField(max_length=100)
    description = models.fields.TextField(null=True)
    year = models.fields.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    offer_type = models.fields.CharField(choices=OfferType.choices, max_length=7)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
