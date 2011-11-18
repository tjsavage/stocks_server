from decimal import *

from django.http import HttpResponse, HttpResponseRedirect

from pystockquotes import quotes

def index(request, symbol):
    info = quotes.get_all(symbol)
    print info
    return HttpResponse(str(info))
    
def current_price(request, symbol):
    price = Decimal(quotes.current_price(symbol))
    
    return HttpResponse(price)
    