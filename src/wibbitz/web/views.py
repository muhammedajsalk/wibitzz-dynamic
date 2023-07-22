from django.shortcuts import render
from web.models import Customer


def index(request):
    customer = Customer.objects.all()
    context={
        "customers" : customer
    }
    return render(request,"index.html",context=context)
