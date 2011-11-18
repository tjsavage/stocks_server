from django.db import models

from portfolio.models import Portfolio, Position

class PortfolioSnapshot(models.Model):
    portfolio = models.ForeignKey(Portfolio)
    date = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    
    def positions(self):
        return PositionSnapshot.objects.filter(portfolio_snapshot=self.pk)
        
    def to_json(self):
        json = "{'portfolio_id':%d, 'date':'%s', 'value':%f}" % (self.pk, str(self.date), self.value)
    
class PositionSnapshot(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    shares = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    share_price = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    portfolio_snapshot = models.ForeignKey(PortfolioSnapshot)
    
    def value(self):
        return self.shares * self.share_price
        

def create_snapshot(portfolio):
    portfolio_snapshot = PortfolioSnapshot(portfolio=portfolio.pk, value=portfolio.current_value())
    portfolio_snapshot.save()
    for position in portfolio.positions():
        position = PositionSnapshot(shares=position.shares,share_price=position.current_price(), portfolio_snapshot=portfolio_snapshot.pk)
        position.save()
    
    return portfolio_snapshot