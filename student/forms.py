from django.core import validators
from django import forms
from .models import City_master, State_master, Student_master


GENDER = (

    ('Male','Male'),
    ('Female','Female'),
)

STATE_CHOICES = (

    ('Maharashtra','Maharashtra'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Gujrat','Gujrat'),
  
)

CITY_CHOICES = (

    ('Pune','Pune'),
    ('Mumbai','Mumbai'),
    ('Lakhnau','Lakhnau'),
    ('Ahemadabad','Ahemadabad')
)


class StudentRegistration(forms.ModelForm):

 city = forms.ModelChoiceField(queryset=City_master.objects.all())
 state = forms.ModelChoiceField(queryset=State_master.objects.all())
 gender = forms.ChoiceField(choices=GENDER,initial='Male')

 class Meta:
  model = Student_master
  fields = ['student_f_name', 'student_m_name', 'student_l_name','state','city','gender']
  labels = {'student_f_name':'First Name', 'student_m_name':'Middle Name', 'student_l_name':'Last Name','state':'State Name','city':'City Name','gender':'Gender'}  
  widgets = {
   'student_f_name': forms.TextInput(attrs={'class':'form-control'}),
   'student_m_name': forms.TextInput(attrs={'class':'form-control'}),
   'student_l_name': forms.TextInput(attrs={'class':'form-control'}),
#    'state': forms.TextInput(attrs={'class':'form-control'}),
#    'city': forms.TextInput(attrs={'class':'form-control'}),
#    'gender': forms.TextInput(attrs={'class':'form-control'}) 
            }


# class CityRegistration(StudentRegistration):

#  city = forms.ChoiceField(choices=CITY_CHOICES,initial='Pune')
#  class Meta:
#   model = City_master 
#   fields = ['city']

# class StateRegistration(StudentRegistration):
 
#  state = forms.ChoiceField(choices=STATE_CHOICES,initial='Maharashtra')
#  class Meta:
#   model = State_master 
#   fields = ['state']
  