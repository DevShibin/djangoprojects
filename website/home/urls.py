from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [path('',views.index,name='index'),
               path('signin',views.signin,name='signin'),
               path('additems',views.additems,name='additems'),
               path('signup',views.signup,name='signup'),     
               path('viewitems',views.viewitems,name='viewitems'),
               path('signout',views.signout,name='signout'),
              ]