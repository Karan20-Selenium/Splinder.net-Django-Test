from django.db import models

# Create your models here.

class City_master(models.Model):

    city_id = models.IntegerField(primary_key = True, max_length=5, default=None)
    city = models.CharField(max_length=20, default=None)

    def __str__(self):

        return self.city

class State_master(models.Model):

    state_id = models.IntegerField(primary_key = True, max_length=5, default=None)
    state = models.CharField(max_length=20, default=None)

    def __str__(self):

        return self.state


GENDER = (

    ('Male','Male'),
    ('Female','Female'),

)
class Student_master(models.Model):

    city = models.ForeignKey(City_master, on_delete= models.PROTECT)
    state = models.ForeignKey(State_master, on_delete= models.PROTECT)

    student_id = models.IntegerField(primary_key = True, max_length=5, default=None)
    student_f_name = models.CharField(max_length=20, default=None)
    student_m_name = models.CharField(max_length=20, default=None)
    student_l_name = models.CharField(max_length=20, default=None)
    gender = models.CharField(max_length=10,choices=GENDER, default='Male')





    


