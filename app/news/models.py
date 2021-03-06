from django.db import models

# Create your models here.
class ContentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
        
class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=True, max_length = 50)
    content = models.CharField(max_length=5000)
    publish_date = models.DateTimeField('date published')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.SET_NULL)
    #image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

