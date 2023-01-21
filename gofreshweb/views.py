from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp5.models import categorydb,productdb
from gofreshweb.models import CustomerDetails,adcontact
# Create your views here.
def firstweb(request):
    return HttpResponse("hello")
def webindex(request):
    data=categorydb.objects.all()
    return render(request,"website_index.html",{'data':data})
def contactus(request):
    data = categorydb.objects.all()
    return render(request, "contact_us.html",{'data':data})
def aboutus(request):
    data = categorydb.objects.all()
    return render(request, "about.html",{'data':data})

def products(request):
    products=productdb.objects.all()
    data = categorydb.objects.all()

    return render(request,"product.html",{'products':products,'data':data})

def discategory(request,itemCatg):
    data = categorydb.objects.all()
    print("===itemCatg===",itemCatg)
    catg=itemCatg.upper()
    products = productdb.objects.filter(category=itemCatg)
    context={
        'products':products,
        'catg':catg,
        'data':data
    }

    return render(request,"display_category.html",context)
def productdetails(request,dataid):
    datas=productdb.objects.get(id=dataid)
    data = categorydb.objects.all()
    return render(request, "product_details.html",{'dat':datas,'data':data})



def weblogin(request):
    data = categorydb.objects.all()
    return render(request, "website_login.html", {'data': data})
def cart(request):
    data = categorydb.objects.all()
    return render(request,"website_cart.html", {'data': data})
def regdata(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        confirm_password=request.POST.get('pass2')
        if password==confirm_password:
            obj=CustomerDetails(username=username,email=email,password=password,confirm_password=confirm_password)
            obj.save()
            return redirect(weblogin)
        else:
            return render(request,'website_login.html',{'msg':"sorry password not matched"})

def customerlogin(request):
    if request.method=='POST':
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")
        if CustomerDetails.objects.filter(username=username_r,password=password_r).exists():
            data=CustomerDetails.objects.filter(username=username_r,password=password_r).values('email','id').first()
            request.session['username']=username_r
            request.session['password']=password_r


            return redirect(webindex)
        else:
            return render(request,'website_login.html',{'msg':"sorry...invalid paasword or username"})
def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(webindex)
def adcontactsave(request):
    if request.method == "POST":
        na = request.POST.get('name')

        em = request.POST.get('email')

        ms = request.POST.get('message')

        obj = adcontact(name=na,email=em,message=ms )
        obj.save()
        return redirect(contactus)







