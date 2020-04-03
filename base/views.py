from django.shortcuts import render, redirect, reverse
from stripeIntegration.local_settings import STRIPE_KEY
from django.views.generic import ListView 
from .models import Event



import stripe
#Your Stripe Key
stripe.api_key = STRIPE_KEY

import requests 
URL = "https://www.worldometers.info/coronavirus/"


# Create your views here.
class EventListView(ListView):
    model = Event 
    template_name = 'base.html'
    queryset = Event.future_events.all()[:4]
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ongoing_events'] = self.model.ongoing_events.all()[:4]
        return context
        



def charge(request):
    
    if request.method == 'POST':
        
        
        amount = float(request.POST['amount']) * 100
        customer = stripe.Customer.create(
            email = request.POST['email'],
            name = request.POST['name'], 
            source = request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer = customer, 
            amount = int(amount),
            currency="usd",
            description = "Donation"
        )
    return redirect('success',int(amount))


def success_msg(request, amount):
    return render(request, 'success.html', {'amount':amount})

