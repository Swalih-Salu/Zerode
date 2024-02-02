from django.urls import path
from . import views
app_name='cart'
urlpatterns = [
    path('cart/<int:id>',views.addCart,name='cart'),
    path('display/',views.display,name='display'),
    path('remove/<int:id>/',views.Remove,name='remove'),
    path('delete/<int:id>/',views.Delete,name='delete'),
    path('buy/',views.Buy,name='buy'),
    
]
