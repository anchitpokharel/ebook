from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('accountspayable/', views.accounts_payable),
    path('invoice/', views.invoice),
    path('payroll/', views.payroll),
    path('reconciliation/', views.reconciliation),
    path('reporting/', views.reporting),
    path('setup_training/', views.setup_training),
    path('virtual_bookkeeping/', views.virtual_bookkeeping),
    path('create_order/', views.create_order, name='create_order'),
]
