import json

from django.shortcuts import render
from web.models import Customer,Subscribe
from django.http import HttpResponse


def index(request):
    customer = Customer.objects.all()
    context={
        "customers" : customer
    }
    return render(request,"index.html",context=context)


def subscribe(request):
    email = request.POST.get("email")
    
    if not Subscribe.objects.filter(email=email).exists():
        
        Subscribe.objects.create(
          email = email
        )

        response_data={
            "status" : "success",
            "title" : "Successfully Registered",
            "message" : "You Subscribed to our newsletter successfully"
        }
    else:
        response_data={
            "status" : "error",
            "title" : "You are already subscribed",
            "message" : "You are already member. No need to register again"
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")