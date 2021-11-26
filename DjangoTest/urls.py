from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.addstudentdata, name="addstudentdata"),
    path('show_data/',views.show_data,name="showdata")
    
]
