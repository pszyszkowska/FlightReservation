from django.shortcuts import render, redirect
import re

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
def clientRegistration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            result = form.save()
            print("test")
            print(result)
            messages.success(request, 'Successfully registered, now u can log in')
            return redirect("/flightSearch")
        else:
            reformattedErrors = str(form.errors).replace("<ul class=\"errorlist\">", "")
            reformattedErrors = re.sub("<li>.*?<li>", "", reformattedErrors)
            reformattedErrors = reformattedErrors.replace("</li></ul></li></ul>", "")
            reformattedErrors = reformattedErrors.split("</li></ul></li>")
            for error in reformattedErrors:
                messages.add_message(request, messages.ERROR, error)
            return render(request, "registration.html")
    else:

        form = UserCreationForm()

    return render(request, "registration.html", {"form": form})


def clientLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():

            login(request, form.get_user())
            messages.success(request, 'Successfully logged in')
            return redirect("/flightSearch")
        else:
            messages.warning(request, 'Incorrect login or password')
            return redirect("/flightSearch")
    else:
        return redirect("/flightSearch")


def clientLogout(request):
    if request.method == "POST":
        logout(request)
        messages.info(request, 'Successfully logged out')
        return redirect("/flightSearch")
