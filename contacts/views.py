from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.


def contacts(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email,
                          realtor_email=realtor_email, message=message,
                          user_id=user_id, phone=phone)
        contact.save()

        messages.info(
            request, "Inquiry has been sent,a realtor will get back to you soon")
        return redirect("/listings/"+listing_id)

    return render(request, "accounts/dashboard.html")
