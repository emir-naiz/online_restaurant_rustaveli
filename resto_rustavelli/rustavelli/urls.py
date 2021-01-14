from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('meals', MealViewsets)
router.register('order', OrderViewsets)
router.register('staff', StaffViewsets)
router.register('bill', BillViewsets)

urlpatterns = [
    # path('views/', MealViews.as_view()),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)