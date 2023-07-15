from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


# @unauthenticated_user
def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "Autentication/login.html", {
                "error": "username veya parola yanlis"
            })
    else:
        return render(request, "Autentication/login.html")


def logoutUser(request):
    logout(request)
    return redirect("login")



