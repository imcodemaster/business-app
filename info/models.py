from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



# Create your models here.

Department = [
                ('Sales & Services', "Sales & Services"),
                ('Account', "Account"),
                ('Tech Support', "Tech Support"),
                ('Build your Business', "Build your Business"),
                ('Customer Executive', "Customer Executive"),

                 
        ]

#contact model for front end 

class Contact(models.Model):
    first_name = models.CharField(max_length = 100)
    second_name = models.CharField(max_length = 100)
    to_the_department = models.CharField( max_length = 30 , choices=Department , null=True , blank=True)
    email = models.EmailField() 
    mobile = models.CharField(max_length = 10)
    message = models.TextField()
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.first_name 


