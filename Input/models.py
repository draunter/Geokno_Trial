from django.db import models
import gdal


# Create your models here.


class AirborneLidar(models.Model):
    type = models.CharField(max_length=100)
    Accuracy = models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    genre = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    genre = models.CharField(max_length=100)
    def __str__(self):
        return self.title +" "+ self.singer
class Son(models.Model):
    songTitle= models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    favorite = models.BooleanField(default=False)


class DEM(models.Model):

    album = models.ForeignKey(Album,on_delete=models.CASCADE,null=True)
    son = models.ForeignKey(Son,on_delete=models.CASCADE,null=True)
    Lidar = models.ForeignKey(AirborneLidar,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=100)
    Accuracy = models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    genre = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

