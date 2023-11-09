from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def sadakah_func(request):
    if request.method == 'POST':
        contact_name = request.POST.get('contact_name')
        contact_email= request.POST.get('contact_email')
        number=request.POST.get('number')
        amount=request.POST['amount']
        madhom=request.POST.get('donete_madhom')
        Tid=request.POST.get('TransactionID')
        sadakahdata = sadakah(name=contact_name, email=contact_email,number=number,amount=amount,madhom=madhom,TransactionID=Tid)
        sadakahdata.save()
        messages.success(request,"জাঝাকাল্লাহ খাইরান")
        return redirect('home')
    return render(request, 'sadakah/sadakah_wrap.html')
    