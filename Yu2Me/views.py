from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    hasSession = request.session.get("logged")
    if hasSession:
        return render(request, 'index.html')
    else:
        # if has no session take to login page
        return redirect(login)

def login(request):
    # Redirect on successful login
    # return redirect(index)
    if request.method == "POST":
        pass
    else:
        return render(request, 'login.html')



