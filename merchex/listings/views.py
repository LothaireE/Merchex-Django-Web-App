from django.shortcuts import render
from listings.models import Band, Offer
from listings.forms import ContactUsForm, BandForm, OfferForm
from django.core.mail import send_mail
from django.shortcuts import redirect 
from django.views.generic import ListView
# Create your views here.
def home(request):

    bands = Band.objects.all()
    toto = ''
    for band in bands : 
        toto += f'<div>{band.name}</div>'

    return render(request, 'listings/home.html', {'bands': bands})    
    # return render(request, 'listings/home.html')


# *************************************************
# ******************* BLOC BAND *******************

class BandListView(ListView):
    model: object = Band
    template_name: str = 'listings/band_list.html'
    context_object_name: str = 'bands'


# def band_list(request):
#     bands = Band.objects.all()
#     return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, band_id): 
    band = Band.objects.get(id=band_id)  # nous insérons cette ligne pour obtenir le Band avec cet id
    print(band)
    return render(request, 'listings/band_detail.html', {'band' : band })


def band_add(request): 

    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:        
        form = BandForm()
    
    return render(request, 'listings/band_add.html', {'form': form})

def band_update(request, band_id): 
    band = Band.objects.get(id=band_id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance = band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance = band)
    
    return render(request, 'listings/band_update.html',{'form': form})

def band_remove(request, band_id):
    band = Band.objects.get(id=band_id)

    if request.method == 'POST':
        band.delete()
        return redirect('band-list')

    return render(request, 'listings/band_remove.html', {'band' : band })

# *************************************************
# ******************* BLOC OFFER ******************

class OfferListView(ListView):
    model: object = Offer
    template_name: str = 'listings/offer_list.html'
    context_object_name: str = 'offers'

# def offer_list(request):

#     offers = Offer.objects.all()

#     return render(request, 'listings/offer_list.html', {'offers': offers})


def offer_detail(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    return render(request,'listings/offer_detail.html', {'offer': offer})

def offer_add(request):

    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save()
            return redirect('offer-detail', offer.id)
    else:
        form = OfferForm()

    form = OfferForm()

    return render(request, 'listings/offer_add.html',{'form': form})

def offer_update(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    
    if request.method == 'POST':
        form = OfferForm(request.POST, instance = offer)
        if form.is_valid():
            offer = form.save()
            return redirect('offer-detail', offer.id)
    else:
        form = OfferForm(instance = offer)

    return render(request, 'listings/offer_update.html', {'form' : form})

def offer_remove(request, offer_id):
    offer = Offer.objects.get(id = offer_id)

    if request.method == 'POST':
        offer.delete()
        return redirect('offer-list')

    return render(request, 'listings/offer_remove.html', {'offer' : offer})


def about(request):

    return render(request, 'listings/about.html')


def contact(request):


    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject= f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message= form.cleaned_data['message'],
                from_email= form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            # return redirect('about')
            return redirect('email-sent')

    else:
        form = ContactUsForm() 


    return render(request,'listings/contact.html',{'form': form})


def email_sent(request):

    return render(request, 'listings/email_sent.html')