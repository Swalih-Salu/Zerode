from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField()
    image=models.ImageField(upload_to='cat_banner')
    
    class Meta:
        ordering=('name',)
        verbose_name='Category'
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('home:prod_by_cat',args=[self.slug])
    
class Product(models.Model):
    image=models.ImageField(upload_to='prdct_img')
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField()
    details=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering=('name',)
        verbose_name='Product'
        verbose_name_plural='Products'
    def __str__(self):
        return self.name
    
class Details(models.Model):
    address=models.TextField()
    pincode=models.IntegerField()
    city=models.TextField()
    country=models.TextField()  
    phone=models.IntegerField()
    
        
    def _str_(self):
        return '{}'.format(self.name)