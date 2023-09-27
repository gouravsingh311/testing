from django.db import models


class Musician(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    instrument=models.CharField(max_length=100)

    def musician_create(self,first_name,last_name,instrument):
        obj = Musician(first_name = first_name,last_name = last_name,instrument = instrument)
        aa = obj.save()
        return aa



class Album(models.Model):
    artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    release_date = models.DateField()
    num_stars = models.ImageField()

class Persons(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Fruit(models.Model):
    name = models.CharField(max_length=30 , primary_key=True)


class Reporter(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    def __str__(self) -> str:
        return f'{self.first_name}{self.last_name}'
    
class Artical(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter , on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.headline
    class Meta:
        ordering = ["headline"]



