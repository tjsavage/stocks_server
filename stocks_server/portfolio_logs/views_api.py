from decimal import *

from django.http import HttpResponse, HttpResponseRedirect

from portfolio_logs.models import PortfolioSnapshot

def portfolio(request, portfolio_id):
    portfolio_snapshots = PortfolioSnapshot.objects.filter(portfolio=portfolio_id).order_by("-date")
    
    json = "{["
    for snapshot in portfolio_snapshots:
        json += snapshot.to_json
        if snapshot != portfolio_snapshots[-1]:
            json += ","
    json += "]}"
    
    return HttpResponse(json)
    