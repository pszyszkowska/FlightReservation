from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

def submitted(request):
    if request.method == "POST":
        messages.info(request, 'Successfully submitted, redirecting to the main page')
        return render(request, "contactform.html")
    else:
        return render(request, "contactform.html")