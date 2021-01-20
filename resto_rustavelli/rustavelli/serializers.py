from rest_framework import serializers
from .models import Meals, Order, Staff, Bill


class MealSerializer(serializers.ModelSerializer):
    price_sale = serializers.SerializerMethodField('get_price_sale')

    class Meta:
        model = Meals
        fields = ['id', 'image', 'name', 'description', 'price', 'rate', 'sale', 'price_sale']

    def get_price_sale(self, obj):
        if obj.sale:
            return obj.price - obj.price * 0.2
        return obj.price

class OrderSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    waiter = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Order
        fields = ['id', 'meal', 'table', 'waiter', 'status']


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'image', 'name', 'role', 'exp']

class BillSerializer(serializers.ModelSerializer):
    bill = serializers.SerializerMethodField('get_total_price_sale')

    class Meta:
        model = Bill
        fields = '__all__'

    def get_total_price_sale(self, obj):
        total = 0
        table = 0
        sale = 0
        orders = Order.objects.all()
        # for order in orders:
        #     total += order.meal.price
        # # total = obj.order.meal.price + (obj.price * 0.15)
        # return total

        for order in orders:
            total += order.meal.price
            sale = total - total * 15 // 100

        return sale









