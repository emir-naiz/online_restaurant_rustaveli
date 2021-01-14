from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views

from .serializers import *
from .models import *
from rest_framework.decorators import api_view

class MealViewsets(viewsets.ModelViewSet):
    queryset = Meals.objects.all()
    serializer_class = MealSerializer

class OrderViewsets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class StaffViewsets(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class BillViewsets(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

