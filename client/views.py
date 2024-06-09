from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout


# Create your views here.
def clientRegistration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered, now u can log in')
            return redirect("/flightSearch")
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
