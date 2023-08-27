
from django.urls import path , include
from . import views
from django.conf import settings



app_name = 'myapp'
urlpatterns = [
    path('' , views.products , name="products") ,
    path('products/add' , views.add_product , name="add_product") ,
    path('products/update/<str:id>' , views.update_product , name="update_product") ,
    path('products/delete/<str:id>' , views.delete_product , name="delete_product") ,
    path('product/<str:id>' , views.product , name='product_detail'),
    
]  
