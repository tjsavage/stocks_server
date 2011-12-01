from django.contrib import admin
from stocks_server.portfolio_logs.models import PortfolioSnapshot, PositionSnapshot

admin.site.register(PortfolioSnapshot)
admin.site.register(PositionSnapshot)