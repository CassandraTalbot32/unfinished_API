from django.shortcuts import render
import requests
API_KEY = 'd3f2194bc218cd398dff1daabc83b4c95a74ad9e'

def location(request):
    url = f'https://epc.opendatacommunities.org/api/v1/display/search?size=1000&from=1000?address=in&LMK_KEY={API_KEY}'
    response = requests.get(url).json()
    rating = response.json()
    
    address = rating['address']

    context = {
    'rating' : rating
    }

    return render(request, 'epc_ratings/location.html', context)


 
