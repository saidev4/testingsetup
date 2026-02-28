from django.db import models

# Create your models here.
class students(models.Model):
    user_name = models.CharField(max_length= 40)
    user_age = models.IntegerField()
    
    
    def __str___(self):
        return self.user_name 
