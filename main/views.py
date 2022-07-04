from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .models import *
# Create your views here.


def home(request):
    return render(request, 'index5.html')


def products(request):
    products = Products.objects.all()
    return render(request, 'products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        product = Products.objects.create(
            name=request.POST['name'],
            amount=request.POST['amount'],
            price=request.POST['price'],
            cr_by=request.user
        )
        product.save()
        return redirect('/products')
    return render(request, 'Products_add.html')

def edit_product(request, id):
    product = Products.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.amount = request.POST['amount']
        product.price = request.POST['price']
        product.cr_by = request.user
        product.save()
        return redirect('/products')
    return render(request, 'products_edit.html', {'product': product})

def delete_product(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('/products')



def client(request):
    clients = Client.objects.all()
    return render(request, 'Clients.html', {'clients': clients})


def add_client(request):
    if request.method == 'POST':
        client = Client.objects.create(
            full_name=request.POST['full_name'],
            address=request.POST['address'],
            phone_number=request.POST['phone'],
            cr_by=request.user
        )
        client.save()
        return redirect('/clients')
    return render(request, 'Clients_add.html')


def edit_client(request, id):
    client = Client.objects.get(id=id)
    if request.method == 'POST':
        client.full_name = request.POST['full_name']
        client.address = request.POST['address']
        client.phone_number = request.POST['phone']
        client.cr_by = request.user
        client.save()
        return redirect('/clients')
    return render(request, 'Clients_edit.html', {'client': client})


def delete_client(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect('/clients')


def raw_material(request):
    materials = RawMaterial.objects.all()
    return render(request, 'rawmaterial.html', {'materials': materials})

def add_raw_material(request):
    if request.method == 'POST':
        material = RawMaterial.objects.create(
            material_name=request.POST['name'],
            size=request.POST['size'],
            price=request.POST['price'],
            cr_by=request.user
        )
        material.save()
        return redirect('/raw_material')
    return render(request, 'material_add.html')

def edit_material(request, id):
    material = RawMaterial.objects.get(id=id)
    if request.method == 'POST':
        material.material_name = request.POST['name']
        material.size = request.POST['size']
        material.price = request.POST['price']
        material.cr_by = request.user
        material.save()
        return redirect('/raw_material')
    return render(request, 'materials_edit.html', {'material': material})

def delete_material(request, id):
    material = RawMaterial.objects.get(id=id)
    material.delete()
    return redirect('/raw_material')

def user_login(request):
    if request.method == 'POST':
        print(request.POST['username'], request.POST['password'])
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("Your account is disabled")
        else:
            return render(request, 'authentication-signin.html', {"error": "Incorrect username or password"})
    else:
        return render(request, 'authentication-signin.html', {})
