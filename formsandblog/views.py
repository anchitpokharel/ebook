from django.shortcuts import render

from formsandblog.models import Contact_us

# Create your views here.
def index(request):
    return render(request, 'index.html')

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
    return render(request, 'setup_training.html')

def virtual_bookkeeping(request):
    return render(request, 'virtual_bookkeeping.html')

def create_order(request):
    if request.method == 'POST':
        your_name = request.POST.get('your_name')
        your_number = request.POST.get('your_number')
        your_email = request.POST.get('your_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        flag = request.POST.get('flag')
        splitted_flag = flag.split("/")
        splitted_flag_path = splitted_flag[1]
        
        save_obj = Contact_us(your_name=your_name, your_number=your_number, your_email=your_email, subject=subject, message=message, flag="")
        save_obj.save()        
    return render(request, f'{splitted_flag_path}.html')