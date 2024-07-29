from django.db import models

class Lead(models.Model):
    added_on = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class FAQ(models.Model):
    added_on = models.DateField(auto_now_add=True)
    question = models.CharField(max_length=1000)
    answer = models.TextField(max_length=500)

    def __str__(self):
        return self.question
