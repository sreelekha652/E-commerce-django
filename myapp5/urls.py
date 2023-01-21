from django.urls import path
from myapp5 import views

urlpatterns=[
    path('first/',views.first,name="first"),
    path('indexpage',views.indexpage,name="indexpage"),
    path('addadmin/',views.addadmin,name="addadmin"),
    path('adminsave/',views.adminsave,name="adminsave"),
    path('admindisplay/',views.admindisplay,name="admindisplay"),
    path('editpage/<int:dataid>/',views.editpage,name="editpage"),
    path('updateadmin/<int:dataid>/',views.updateadmin,name="updateadmin"),
    path('deleteadmin/<int:dataid>/',views.deleteadmin,name="deleteadmin"),
    path('addcategory/',views.addcategory,name="addcategory"),
    path(' catesave/',views.catesave,name="catesave"),
    path('categorytable/',views.categorytable,name="categorytable"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('updatecategory/<int:dataid>/',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:dataid>/',views.deletecategory,name="deletecategory"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('productsave/',views.productsave,name="productsave"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('editproduct/<int:dataid>/',views.editproduct,name="editproduct"),
    path('updateproduct/<int:dataid>/',views.updateproduct,name="updateproduct"),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name="deleteproduct"),
    path('adlogin/',views.adlogin,name="adlogin"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('contact/',views.contact,name="contact")



]