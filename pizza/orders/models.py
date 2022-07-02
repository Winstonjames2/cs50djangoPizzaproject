from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
class FoodType(models.Model):
    name=models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.name}"

class Size(models.Model):
    name=models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.name}"

class Feature(models.Model):
    name=models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.name}"

class Food(models.Model):
    foodtype=models.ForeignKey(FoodType,on_delete=models.CASCADE,related_name="types")
    feature=models.ForeignKey(Feature,on_delete=models.CASCADE,related_name="feature")
    size=models.ForeignKey(Size,on_delete=models.CASCADE,related_name="size")
    price=models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"{self.id},{self.foodtype}-{self.feature},{self.size},${self.price}"
    
class Cart(models.Model):
    user_id=models.IntegerField()
    username=models.CharField(max_length=64)
    food=models.ManyToManyField(Food,blank=True, related_name="food")
    
    def __str__(self):
        return f"UserID - {self.user_id}, Username: {self.username}"

class Times(models.Model):
    user_id=models.IntegerField()
    food_id=models.IntegerField()
    times=models.IntegerField(default=0)

    def __str__(self):
        return f"UserID - {self.user_id}, FoodID - {self.food_id}, {self.times} times"