from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100) #, blank=True,null=True)
    content=models.TextField()
    img = models.ImageField(upload_to = "static/media/")

    def __str__(self):
        return self.title