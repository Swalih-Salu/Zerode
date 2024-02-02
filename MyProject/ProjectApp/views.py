from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Category,Details
from django.core.paginator import Paginator,InvalidPage,EmptyPage

# Create your views here.
def Home(req,c_slug=None):
    c_page=None
    Product_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        Product_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        Product_list=Product.objects.all().filter(available=True)
        
        
    paginator=Paginator(Product_list,8)
    try:
       page=int(req.GET.get('page',))
    except:
       page=1
    try:
       product=paginator.page(page)
    except(EmptyPage,InvalidPage):
       product=paginator.page(paginator.num_pages)  

    return render(req,'index.html',{"product":product,"cat":c_page})

# def Addnew(req):
#     if req.method=='POST':
#         image=req.FILES['image']
#         image1=req.FILES['image1']
#         image2=req.FILES['image2']
#         image3=req.FILES['image3']
#         image4=req.FILES['image4']
#         name=req.POST.get('name')
#         desc=req.POST.get('desc')
#         details=req.POST.get('details')
#         rating=req.POST.get('rating')
#         price=req.POST.get('price')
#         category=
#         stock=req.POST.get('stock')

def details(req,id):
   data=Product.objects.get(id=id)
   return render(req,"details.html",{'data':data})

def About(req):
   return render(req,"about.html")     
def Profile(req):
   detail=Details.objects.all()
   return render(req,'profile.html',{'data':detail})

def Address(request):
   
     detail=None
     if request.method == 'POST':
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        print(address,pincode,city,country,phone)
        detail=Details(address=address, pincode=pincode, city=city, country=country, phone=phone)
        detail.save()
        return redirect('home:profile')
     return render(request,'address.html',{'data':detail})
  
def delete(request,id):

        details=Details.objects.get(id=id)
        details.delete()
        return redirect('home:profile')