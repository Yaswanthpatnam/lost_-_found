from django.db import models

# Create your models here.

class LostItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='lost_images/', blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    contact_info = models.CharField(max_length=100)
    date_lost = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Lost: {self.title} - {self.date_lost.strftime('%Y-%m-%d %H:%M')}"
    
    
class FoundItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()    
    image = models.ImageField(upload_to='lost_images/', blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    contact_info = models.CharField(max_length=100)
    date_found = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Found: {self.title} - {self.date_found.strftime('%Y-%m-%d %H:%M')}"