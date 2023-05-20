from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    created_at = models.DateTimeField()
    # author : 추후 작성
    
    def __str__(self):
        return f'[{self.pk}]{self.title}'

# Create your models here.
