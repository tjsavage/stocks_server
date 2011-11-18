from django.contrib import admin
from stocks_server.portfolio.models import Portfolio, Position

class PortfolioAdmin(admin.ModelAdmin):
    pass
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Position)