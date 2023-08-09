from django.shortcuts import render
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework import generics

class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class=CustomerSerializer

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class =OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
# Create your views here.
