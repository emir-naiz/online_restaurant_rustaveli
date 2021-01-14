from django.db import models

# Create your models here.

class Meals(models.Model):
    rating = (
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
    )
    image = models.ImageField(blank=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    rate = models.CharField(choices=rating, max_length=50)
    sale = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

class Order(models.Model):
    status = (
        ('ready', 'ready'),
        ('in process', 'in process'),
        ('not ready', 'not ready'),
        ('closed', 'closed')
    )
    meal = models.ForeignKey(Meals, on_delete=models.SET_NULL, null=True, related_name='orders')
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=status, max_length=100)
    table = models.IntegerField()
    waiter = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, related_name='staff')

    def __str__(self):
        return self.meal.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Staff(models.Model):
    role = (
        ('chef', 'chef'),
        ('waiter', 'waiter'),
        ('manager', 'manager'),
        ('bartender', 'bartender')
    )

    exp = (
        ('beginner', 'beginner'),
        ('middle', 'middle'),
        ('master', 'master'),
    )
    name = models.CharField(max_length=200)
    role = models.CharField(choices=role, max_length=100)
    exp = models.CharField(choices=exp, max_length=20)
    image = models.ImageField()
    date_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + '' + self.role

    class Meta:
        verbose_name = 'Персонала'
        verbose_name_plural = 'Персонал'

class Bill(models.Model):
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, related_name='bill')
    total = models.FloatField()

    # def __str__(self):
    #     return self.order

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'