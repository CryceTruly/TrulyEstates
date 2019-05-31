from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .choices import price_choices, bedroom_choices, state_choices


def index(request):
    listings = Listing.objects.order_by("-list_date")
    paginator = Paginator(listings, 1)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        "listings": paged_listings
    }
    return render(request, "listings/index.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        "listing": listing
    }
    return render(request, "listings/listing.html", context)


def search(request):
    queryset_list = Listing.objects.order_by(
        "-list_date").filter(is_published=True)


# SEARCH BY KEYWORD
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)


# SEARCH BY CITY
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

# SEARCH BY address
    if 'state' in request.GET:
        city = request.GET['state']
        if city:
            queryset_list = queryset_list.filter(
                address__iexact=city)


# SEARCH BY bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)


# SEARCH BY price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    context = {
        "state_choices": state_choices,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "listings": queryset_list
    }
    return render(request, "listings/search.html", context)
