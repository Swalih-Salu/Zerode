from django.db import models
from ProjectApp.models import Product,Details
# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    user_id=models.IntegerField()

class Orders(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    address=models.TextField(max_length=255, null=False)