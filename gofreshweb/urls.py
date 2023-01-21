from django.urls import path
from gofreshweb import views

urlpatterns=[
    path('firstweb/',views.firstweb,name="firstweb"),
    path('',views.webindex,name="webindex"),
    path('contactus/',views.contactus,name="contactus"),
    path('aboutus/',views.aboutus,name="aboutus"),

    path('products/',views.products,name=" products"),
    path('discategory/<itemCatg>',views.discategory,name="discategory"),
    path('productdetails/<int:dataid>',views.productdetails,name="productdetails"),
    path('weblogin/',views.weblogin,name="weblogin"),
    path('cart/',views.cart,name="cart"),
    path('regdata/',views.regdata,name="regdata"),
    path('customerlogin/',views.customerlogin,name="customerlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('adcontactsave/', views.adcontactsave, name="adcontactsave")


]