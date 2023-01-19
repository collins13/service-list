from django.shortcuts import render

# Create your views here.


def create_listing(request):
    return render(request, 'listings/create-listing.html')
