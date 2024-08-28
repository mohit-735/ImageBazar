from django.db import models

# Create your models here.

# create catagories model


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    # Override Magic method
    def __str__(self):
        return self.title     # use for to use show title name like we created catagory in 
                               # admin such as games 

    

# create images model

class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    added_date = models.DateTimeField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    # override magic method for images
    def __str__(self):
        return self.title
    