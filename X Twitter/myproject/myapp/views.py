from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User(email=email, password=password)
        user.save()
        return HttpResponse("Datos guardados en la base de datos")
    else:
        return render(request, 'tu_template.html')
