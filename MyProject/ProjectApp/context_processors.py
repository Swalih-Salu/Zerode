from .models import Category
from cartApp.models import Cart

def menu_link(req):
    links=Category.objects.all()
    return dict(links=links)

def count(req):
    
    try:
        user_id=req.session['user']
        data=Cart.objects.all().filter(user_id=user_id)
        count=data.count()
    except:
        count=0
    return dict(count=count)