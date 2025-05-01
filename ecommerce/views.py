from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Customer
# Create your views here.
def ecommerce_index_view(reqquest):
    '''This func render index page of ecommerce views'''
    return HttpResponse('Welcome to 6510742056 Thitichaya Pounglaowech views!')

def item_view(request, item_id):
    context_data = {
        "item_id": item_id
    }
    return render(request, 'index.html',context= context_data)

def customer_all_view(request):
    customers = list(Customer.objects.all().values())
    return JsonResponse(customers, safe=False)

def view_username(request, username):
    user_data = {
        "email": username.email,
        "username": username.username,
    }
    return JsonResponse(user_data)