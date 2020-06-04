from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Address, STATE_CHOICES
from .forms import AddressForm


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
    form_submitted = False
    if request.method == 'GET':
        form = AddressForm()
        return render(request, 'my_app/address/create.html', {'form': form})
    else:
        form_submitted = True
        form = AddressForm(request.POST)
        if form.is_valid():
            Address.objects.create(
                address=form.cleaned_data['address'],
                address_complement=form.cleaned_data['address_complement'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                country=form.cleaned_data['country'],
                user=request.user
            )
            return redirect('/addresses/')
    return render(request, 'my_app/address/create.html', {
        'form': form, 'form_submitted': form_submitted
    })


@login_required(login_url='/login/')
def address_update(request, id):
    form_submited = False
    address = Address.objects.get(id=id)
    if request.method == 'GET':
        form = AddressForm(address.__dict__)
    else:
        form_submited = True
        form = AddressForm(request.POST)
        if form.is_valid():

            address.address = request.POST.get('address')
            address.address_complement = request.POST.get('address_complement')
            address.city = request.POST.get('city')
            address.state = request.POST.get('state')
            address.country = request.POST.get('country')
            address.save()
            return redirect('/addresses/')
    return render(request, 'my_app/address/update.html', {
        'address': address,
        'form': form,
        'form_submited': form_submited
    })
