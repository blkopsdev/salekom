from django.db import models
from PIL import Image
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='Category_img', blank=True)
    """def get_place(self):
        return place.objects.filter(category=self)"""

    def __str__(self):
        return self.title

class Place(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    location_text = models.CharField(max_length=200, blank=True, default='')
    discount_rate = models.CharField(max_length=200, blank=True, default='')
    image = models.ImageField(upload_to='Place_img', blank=True)

    def __str__(self):
        return self.title
