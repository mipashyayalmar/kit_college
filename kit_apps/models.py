
import django
from kit_apps import models
from django.db import models
from django.db import models
from django.db import models

class StudentSuggestion(models.Model):
    request_id = models.AutoField(primary_key=True)
    added_date = models.DateTimeField(auto_now=True)
    f_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    subject = models.CharField(max_length=60)
    about = models.TextField(max_length=150)

    
    
 
   


  