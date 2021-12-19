from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
# Create your models here.
class Date(models.Model):
    date=models.CharField(max_length=2)
    def __str__(self):
        return self.date
class Month(models.Model):
    month=models.CharField(max_length=10)
    def __str__(self):
        return self.month
class Name (models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    date=models.ForeignKey(Date, on_delete=models.SET_NULL, null=True)
    month=models.ForeignKey(Month, on_delete=models.SET_NULL, null=True)
    flight_no =models.CharField(max_length=50)
    seat_no =models.CharField(max_length=50)
    fromm =models.CharField(max_length=50)
    to =models.CharField( max_length=50)


class Task (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    sub=models.ForeignKey(Name, on_delete=models.SET_NULL, null=True)
    chapter=models.CharField(max_length=200)
    details=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    date=models.ForeignKey(Date, on_delete=models.SET_NULL, null=True)
    month=models.ForeignKey(Month, on_delete=models.SET_NULL, null=True)
    flight_no =models.CharField(max_length=50)
    seat_no =models.CharField(max_length=50)

    class Meta:
        ordering=['complete']
        
