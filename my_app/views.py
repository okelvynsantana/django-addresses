from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Address, STATE_CHOICES


def login(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'my_app/login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        django_login(request, user)
        return redirect('/dashboard/')
    message = 'Usuário ou senha inválidos.'
    return render(request, 'my_app/login.html', {'message': message})


@login_required(login_url='/login/')
def logout(request):
    django_logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'my_app/dashboard.html')


@login_required(login_url='/login/')
def address_list(request):
    addresses = Address.objects.all()
    return render(request,
                  'my_app/address/list.html', {'addresses': addresses})


@login_required(login_url='/login/')
def address_create(request):
    if request.method == 'GET':
        states = STATE_CHOICES
        return render(request, 'my_app/address/create.html', {'states': states})
    Address.objects.create(
        address=request.POST.get('address'),
        address_complement=request.POST.get('address_complement'),
        city=request.POST.get('city'),
        state=request.POST.get('state'),
        country=request.POST.get('country'),
        user=request.user
    )
    return redirect('/addresses/')
