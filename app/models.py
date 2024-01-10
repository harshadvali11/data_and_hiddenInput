from django.db import models

# Create your models here.

class School(models.Model):
    Sname=models.CharField(max_length=100)
    Sprincipal=models.CharField(max_length=100)
    Slocation=models.CharField(max_length=100)
    email=models.EmailField(default='hai@gmail.com')
    renteremail=models.EmailField(default='hai@gmail.com')

    def __str__(self):
        return self.Sname



        