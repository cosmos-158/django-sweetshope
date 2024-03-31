from django.shortcuts import render, HttpResponse, render, redirect
from django.http import JsonResponse
import json

from .ocl import connect_to_db
from .user_input import insert_into_db

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    if request.method == 'POST':
        form_data = request.POST.get('quantity')
    return render(request, 'about.html')

def order(request):
    return render(request, 'order.html')

def calculate_total(request):
    print("Inside calculate fun")
    sweet_name = request.GET.get('sweetName')
    sweet_name = sweet_name.strip().replace(' ', '').upper()
    quantity = request.GET.get('quantity')
    # print(f"{sweet_name} and {quantity}")
    if sweet_name and quantity:
        price = connect_to_db(sweet_name)
        # print(price)
        # print(type(int(price)))
        total = int(quantity)*int(price)
        return JsonResponse({'total': total})

    return JsonResponse({'total': 0})

def showCart(request):
    print("Inside ShowCart")
    jsonData = request.POST.get('cartItem')
    jsonDataString = json.dumps(jsonData)
    print(jsonData)
    context = {
        'jsonData' : jsonDataString
    }
    return render(request, 'cart.html', context)

def user_detail(request):
    fName = request.POST.get('firstname')
    lName = request.POST.get('lastname')
    pno = request.POST.get('phonenumber')
    sub = request.POST.get('subject')
    query = f"Insert Into user_detail (FirstName, LastName, MobileNumber, UserInput) Values( '{fName}', '{lName}', '{pno}', '{sub}')"
    
    insert_into_db(query)

    return redirect('/')

