from django.db import models
# Create your tests here.
class sadakah(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100)
    number=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    TransactionID=models.CharField(max_length=100)
    madhom=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.email