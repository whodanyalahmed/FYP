from scrapper_and_analyzer.backend.priceoye import priceOye_main
from scrapper_and_analyzer.backend.daraz import daraz_main
from django.shortcuts import render
import sys
sys.path.append('../')

# import daraz.py from python folder
# Create your views here.


def home(request):

    return render(request, 'index.html')


def result(request):
    # get browser session storage value

    # get request values
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        print(keyword)
        # call scrapper function
        daraz = daraz_main(keyword)
        priceOye = priceOye_main(keyword)
        print(daraz)
        print(priceOye)
        return render(request, 'results.html', {'daraz': daraz, 'priceOye': priceOye})

    return render(request, 'results.html')
