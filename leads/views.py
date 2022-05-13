from django.shortcuts import render
from django.http import HttpResponse

from .models import Lead

# Create your views here.
def home_page(request):
    context = {
        "name" : "Joe",
        "age" : 35
    }
    leads = Lead.objects.all()
    context1 = {
        "leads":leads
    }
    return render(request, "second_page.html",context1)