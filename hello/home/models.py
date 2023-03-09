from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(("First Name"), max_length=50)
    username=models.CharField(("Username"), max_length=50)
    MobileNumber=models.CharField(("Mobile Number"), max_length=50)
    Gender=models.CharField(("Gender"), max_length=50)
    Email=models.CharField(("Email Id"), max_length=50)
    location=models.CharField(("Location"), max_length=50)
    password=models.CharField(("Enter Password"), max_length=50)
