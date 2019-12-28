from django.db import models

# Create your models here.
class Topic(models.Model):
    """The topics a post can be about""" 
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Post(models.Model):
    """Specific post about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."