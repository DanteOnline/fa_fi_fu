from django.db import models


# Create your models here.
class FoodTime(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class FoodPart(models.Model):
    name = models.CharField(max_length=32)
    food_time = models.ForeignKey(FoodTime)

    class Meta:
        unique_together = (("name", "food_time"),)

    def __str__(self):
        return self.name + '/' + str(self.food_time)


class Food(models.Model):
    name = models.CharField(max_length=32)
    part = models.ForeignKey(FoodPart)


    def __str__(self):
        return self.name + '/' + str(self.part) + '/' + str(self.part.food_time)
