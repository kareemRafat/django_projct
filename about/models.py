from django.db import models
from datetime import datetime
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return self.name

##################
    
class User(models.Model) :
    username = models.CharField(max_length = 20 , null = True , unique = True )
    password = models.CharField(max_length = 20 )
    email = models.CharField(max_length = 50)
    address = models.TextField()
    tall = models.DecimalField(max_digits = 4  , decimal_places = 2)
    registered_at = models.DateTimeField(default = datetime.now())
    profile = models.ImageField(upload_to = 'images/%y/%m/%d' , blank = True)
    # many to one relation # related_name for the relation Department.users.all()
    dep = models.ForeignKey(Department , related_name = 'users' , on_delete = models.CASCADE , null = True)


    def __str__(self) -> str:
        return self.username
    
