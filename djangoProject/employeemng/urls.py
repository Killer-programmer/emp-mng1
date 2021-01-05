from django.urls import path
from .views import *

urlpatterns = [
    path('employeeadd', employeeAdd, name='empadd'),
    path('employeeview', employeeView, name='empview'),
    path('employeeedit/<str:pk>', employeeEdit, name='empedit'),
    path('employeedlt/<str:pk>', employeeDelete, name='empdlt'),
    path('allemployeepdf', render_pdf_view, name='emppdf'),
]
