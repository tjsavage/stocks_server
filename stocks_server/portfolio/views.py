from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from portfolio.models import Portfolio, Position

def index(request):
    portfolios = Portfolio.objects.all()
    
    return render_to_response('portfolio/index.html', { 'portfolios': portfolios })
    
def portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    return render_to_response('portfolio/portfolio.html', { 'portfolio': portfolio })