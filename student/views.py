from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
from student.models import Student_master

# Create your views here.
def addstudentdata(request):
 if request.method == 'POST':
  fm = StudentRegistration(request.POST)
  if fm.is_valid():
   f_name = fm.cleaned_data['student_f_name']
   m_name = fm.cleaned_data['student_m_name']
   l_name = fm.cleaned_data['student_l_name']
   state = fm.cleaned_data['state']
   city = fm.cleaned_data['city']
   gender = fm.cleaned_data['gender']

   reg = Student_master(student_f_name = f_name, student_m_name = m_name, student_l_name = l_name ,state = state, city = city, gender = gender)
   reg.save()
   return HttpResponseRedirect('/show_data')

   fm = StudentRegistration()
 else:
  fm = StudentRegistration()
  
 return render(request, 'base.html', {'form':fm})

def show_data(request):

 if request.method == 'GET':
  studs = Student_master.objects.all()
  return render(request, 'show_data.html', {'studs':studs})

