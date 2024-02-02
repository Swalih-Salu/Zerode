from django.urls import path
from . import views

app_name='home'
urlpatterns = [
    path('',views.Home,name='Homem'),
    # path('<slug:c_slug>/',views.Home,name='prod_by_cat'),
    path('details/<int:id>/',views.details,name='details'),
    path('about/',views.About,name='about'),
    path('profile/',views.Profile,name='profile'),
    path('addaddress/',views.Address,name='address'),
    path('delete/<int:id>/',views.delete,name='delete'),
   
]
