from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                    self).get_queryset().filter(status='published')

class Newsletter(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'),)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique_for_date='publish', max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myapp_Newsletter')
    date = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('myapp:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

                        
# class Newsletter(models.Model):
    # ...
    
    
# class Newsletter(models.Model):
    # ...
    