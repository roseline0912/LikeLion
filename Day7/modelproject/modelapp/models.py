from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField('내용')
    created_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title