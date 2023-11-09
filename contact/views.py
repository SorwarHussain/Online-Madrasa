from django.shortcuts import render
from .models import contactus
from django.contrib import messages
# Create your views here.


def contact(request):
    if request.method == 'POST':
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_subject = request.POST['contact_subject']
        message = request.POST['message']
        contactdata = contactus(
            name=contact_name, email=contact_email, subject=contact_subject, message=message)
        contactdata.save()
        messages.success(request,"আপনার আবেদন সম্পন্ন হয়েছে। আমরা যত শীঘ্র সম্ভব আপনার সাথে যোগাযোগ করার চেষ্টা করবো ইন শা আল্লাহ।")
    return render(request, 'contact_page/contact.html')
