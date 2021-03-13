from django.db import models
from datetime import datetime

# MODELLARIMIZNI SHU YERDA KIRITAMIZ
class BlogPost(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=150,blank=True)
    finished = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now,blank=True) 
    image = models.CharField(max_length=400,default="https://images.unsplash.com/photo-1500989145603-8e7ef71d639e?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1355&q=80")

    def __str__(self):
        return self.title