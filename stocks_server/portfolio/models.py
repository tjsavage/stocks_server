from django.db import models
from django.contrib.auth.models import User

from pystockquotes import quotes
from decimal import *

class Position(models.Model):
    portfolio = models.ForeignKey('Portfolio')
    ticker = models.CharField(max_length=10)
    shares = models.DecimalField(max_digits=15, decimal_places=5)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s: %f shares of %s" % (self.portfolio, self.shares, self.ticker)
        
    def current_value(self):
        return self.shares * Decimal(quotes.current_price(self.ticker))

class Portfolio(models.Model):
    name = models.CharField(max_length=20)
    creator = models.ForeignKey(User, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    initial_cash = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    cash = models.DecimalField(max_digits=15, decimal_places=5, default=0)

    def __unicode__(self):
        return self.name

    def positions(self):
        positions = Position.objects.filter(portfolio=self.pk)
        return positions
    
    def current_value(self):
        value = self.cash
        positions = self.positions()
        if positions:
            for position in self.positions():
                value += position.current_value()
                print position.current_value()
        return value