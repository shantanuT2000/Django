from multiprocessing import context
from tokenize import Name
from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request): 
    # return HttpResponse("This is Homepage")
    #context is set of variables sent to template its a python list
    context={
        'variable':"This is Shantanu"
    }
    # messages.success(request,"this is test message")
    return render(request,'index.html',context)
    
def about(request):
    # return HttpResponse("This is Aboutpage")
    return render(request,'about.html')
def services(request):
    # return HttpResponse("This is Servicespage")
    return render(request,'Services.html')
def contact(request):
    # return HttpResponse("This is contactpage")
    if request.method == "POST":
        name = request.POST.get('Name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request,'contact.html')
    