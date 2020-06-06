from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View, RedirectView
from .forms import AddressForm
from .models import Address
from django.utils.decorators import method_decorator


def home(request):
    return redirect(reverse('address_list'))


class LoginView(View):
    template_name = 'my_app/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            django_login(request, user)
            return redirect(reverse('address_list'))
        message = 'Usuário ou senha inválidos.'
        return render(request, self.template_name, {'message': message})


class LogoutRedirectView(RedirectView):
    url = '/login/'

    @method_decorator(login_required(login_url='/login'))
    def get(self, request, *args, **kwargs):
        django_logout(request)
        return super().get(request, *args, **kwargs)


# @login_required(login_url='login')
# def logout(request):
#     django_logout(request)
#     return redirect(reverse('login'))


@login_required(login_url='login')
def address_list(request):
    addresses = Address.objects.all()
    return render(request,
                  'my_app/address/list.html', {'addresses': addresses})


@login_required(login_url='login')
def address_create(request):
    form_submitted = False
    if request.method == 'GET':
        form = AddressForm()
        return render(request, 'my_app/address/create.html', {'form': form})
    else:
        form_submitted = True
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect(reverse('address_list'))
    return render(request, 'my_app/address/create.html', {
        'form': form, 'form_submitted': form_submitted
    })


@login_required(login_url='/login/')
def address_update(request, id):
    form_submitted = False
    address = Address.objects.get(id=id)
    if request.method == 'GET':
        form = AddressForm(instance=address)
    else:
        form_submitted = True
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect(reverse('address_list'))
    return render(request, 'my_app/address/update.html', {
        'address': address,
        'form': form,
        'form_submitted': form_submitted
    })


@login_required(login_url='login')
def address_destroy(request, id):
    address = Address.objects.get(id=id)
    if request.method == 'GET':
        form = AddressForm(instance=address)
    else:
        address.delete()
        return redirect(reverse('address_list'))
    return render(request, 'my_app/address/destroy.html', {
        'address': address, 'form': form
    })
