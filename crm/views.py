from django.shortcuts import render
from .models import Order
# Create your views here.


def first_page(request):
    return render(request, './index.html')


def contact_user(request):
    return render(request, './contact_us.html')


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    message = request.POST['message']
    element = Order(order_name=name, order_phone=phone, order_email=email, order_message=message)
    element.save()
    return render(request, './thanks_page.html', {'name': name,
                                                  'phone': phone})