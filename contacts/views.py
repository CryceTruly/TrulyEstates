from django.shortcuts import render
from django.contrib import messages

# Create your views here.


def contacts(request):
    messages.info(request, "Inquiry has been sent")

    return render(request, "accounts/dashboard.html")
