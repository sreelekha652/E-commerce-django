from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp5.models import admindatabase, categorydb, productdb
from gofreshweb.models import adcontact
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def first(request):
    return HttpResponse("hello")
def indexpage(request):
    return render(request, "index.html")
def addadmin(request):
    return render(request,"ADDadmin.html")
def adminsave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        mob = request.POST.get('number')
        em = request.POST.get('email')
        img = request.FILES['image']
        ui = request.POST.get('userid')
        psw = request.POST.get('password')
        cpsw = request.POST.get('cpassword')
        obj = admindatabase(name=na, mobile_number=mob, email=em, image=img, userid=ui, password=psw,confirm_password=cpsw)
        obj.save()
        return redirect(addadmin)

def admindisplay(request):
    data=admindatabase.objects.all()
    return render(request,"admin_display.html",{'data':data})

def editpage(request,dataid):
    data = admindatabase.objects.get(id=dataid)
    print(data)
    return render(request, "editadmin.html", {'data': data})
def updateadmin(request,dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        mob = request.POST.get('number')
        em = request.POST.get('email')

        ui = request.POST.get('userid')
        psw = request.POST.get('password')
        cpsw = request.POST.get('cpassword')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = admindatabase.objects.get(id=dataid).image
        admindatabase.objects.filter(id=dataid).update(name=na,mobile_number=mob, email=em, userid=ui, password=psw, confirm_password=cpsw, image=file)
        return redirect(admindisplay)
def deleteadmin(request,dataid):
    data = admindatabase.objects.filter(id=dataid)
    data.delete()
    return redirect(admindisplay)

def addcategory(request):
    return render(request,"add_category.html")
def catesave(request):
    if request.method == "POST":
        catn = request.POST.get('cname')
        dis = request.POST.get('discription')
        img = request.FILES['image']
        obj = categorydb(category_name=catn, discription=dis,image=img)
        obj.save()
        return redirect(addcategory)
def categorytable(request):
    data = categorydb.objects.all()
    return render(request, "category_display.html", {'data': data})
def editcategory(request,dataid):
    data = categorydb.objects.get(id=dataid)
    print(data)
    return render(request, "edit_category.html", {'data': data})
def updatecategory(request,dataid):
    if request.method == "POST":
        catn = request.POST.get('cname')
        dis = request.POST.get('discription')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).image
        categorydb.objects.filter(id=dataid).update(category_name=catn, discription=dis, image=file)
        return redirect(categorytable)
def deletecategory(request,dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(categorytable)

def addproduct(request):
    data = categorydb.objects.all()
    return render(request, "add_product.html", {'data': data})
def productsave(request):
    if request.method == "POST":
        cate = request.POST.get('category')
        pn = request.POST.get('pname')
        pp = request.POST.get('price')
        pq = request.POST.get('quantity')
        img = request.FILES['image']
        obj = productdb(category=cate,productname=pn, productprice_per_kg=pp , product_quantity=pq,image=img)

        obj.save()
        return redirect(addproduct)
def displayproduct(request):
    data = productdb.objects.all()
    return render(request,"product_display.html",{'data':data})
def editproduct(request,dataid):
    data = productdb.objects.get(id=dataid)
    da=categorydb.objects.all()
    print(data)
    return render(request, "edit_product.html", {'data': data,'da':da})
def updateproduct(request,dataid):
    if request.method == "POST":
        cate = request.POST.get('category')
        pn = request.POST.get('pname')
        pp = request.POST.get('price')
        pq = request.POST.get('quantity')

        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).image
        productdb.objects.filter(id=dataid).update(category=cate, productname=pn, productprice_per_kg=pp, product_quantity=pq, image=file)
        return redirect(displayproduct)
def deleteproduct(request,dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)
def adlogin(request):
    return render(request,"login_page.html")
def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")

        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(adlogin)
        else:
            return redirect(adlogin)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adlogin)
def contact(request):
    data = adcontact.objects.all()
    return render(request, "message.html",{'data': data})
