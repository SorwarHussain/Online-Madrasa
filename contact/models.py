from django.db import models

# Create your models here.

class contactus(models.Model):
    name=models.CharField(max_length=100) #, blank=True,null=True)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=700)

    def __str__(self):
        return self.subject