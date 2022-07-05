from django.shortcuts import render

# Create your views here.
def index(request):
    bootstrap_class = "service-homebtn"
    return render(request, 'index.html', {bootstrap_class: bootstrap_class})

def accounts_payable(request):
    return render(request, 'accounts_payable.html')

def invoice(request):
    return render(request, 'invoice.html')

def payroll(request):
    return render(request, 'payroll.html')

def reconciliation(request):
    return render(request, 'reconciliation.html')

def reporting(request):
    return render(request, 'reporting.html')

def setup_training(request):
    return render(request, 'setup-training.html')

def virtual_bookkeeping(request):
    return render(request, 'virtual-bookkeeping.html')