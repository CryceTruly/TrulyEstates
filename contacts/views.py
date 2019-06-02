from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
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

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            # if has_contacted:
            #     messages.error(request,
            #                    message="You have already made an inquirly for this listing")
            #     return redirect("/listings/"+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email,
                          realtor_email=realtor_email, message=message,
                          user_id=user_id, phone=phone)
        contact.save()
        send_mail(
            'Property Listing inquiry',
            'There has been an inquiry for '+listing,
            'crycetruly@gmail.com',
            [realtor_email, "aacryce@gmail.com"],
            fail_silently=False,
        )

        messages.info(
            request, "Inquiry has been sent,a realtor will get back to you soon")
        return redirect("/listings/"+listing_id)

    return render(request, "accounts/dashboard.html")
