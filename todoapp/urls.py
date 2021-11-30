
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path
from todo import views
from todo.views import *

urlpatterns = [
    #####################home_page###########################################
    path('todo/', views.all_todos, name="todo"),
    ####################give id no. item_id name or item_id=i.id ############
    path('del/<int:son>', views.remove, name="del"),
    ########################################################################
    path('admin/', admin.site.urls),
    path('todo/submit', views.index, name='submit' ),
    path('', views.loginView, name='login'),
    path('reg/', views.registration, name='reg'),
    path('logout/', views.logoutView, name='logout')
]
