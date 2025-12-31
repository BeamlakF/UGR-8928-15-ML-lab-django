from django.urls import path
from .views import predict_employee

urlpatterns = [
    path("", predict_employee, name="predict"),
]
