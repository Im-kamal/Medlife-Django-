from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('',views.index,name='about_us'),
    path('',views.index,name='contact_us'),
    path('',views.index,name='products'),
    path('',views.index,name='log_in'),
    path('',views.index,name='sign_up'),
    path('',views.index,name='item'),
]
