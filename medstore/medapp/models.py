
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, default='',null=True)

    def __str__(self):
        return self.user.username
    
    
class Medicine(models.Model):
    medicine_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pics', blank=True)
    expire_date = models.DateField()

    def __str__(self):
        return self.medicine_name
