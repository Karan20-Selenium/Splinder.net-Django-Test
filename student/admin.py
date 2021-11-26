from django.contrib import admin
from .models import City_master, State_master, Student_master

# Register your models here.
@admin.register(City_master)
class City_masterAdmin(admin.ModelAdmin):
 list_display = ('city_id','city')


@admin.register(State_master)
class State_masterAdmin(admin.ModelAdmin):
 list_display = ('state_id','state')

@admin.register(Student_master)
class Student_masterAdmin(admin.ModelAdmin):
 list_display = ('student_id','student_f_name','student_m_name','student_l_name','gender','city','state')
