from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthUserModel(AbstractUser):
    GENDER_CHOICES =[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null = True, blank = True)
    age = models.PositiveIntegerField(null = True, blank = True)
    weight = models.FloatField(null = True, blank = True)
    height = models.FloatField(null = True, blank = True)

    def __str__(self):
        return self.username
    
class CalorieEntryModel(models.Model):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE, related_name='calorie_entries')
    item_name = models.CharField(max_length=250, null = True, blank = True)
    calories_consumed = models.PositiveIntegerField(null = True, blank = True)
    date = models.DateField(auto_now_add= True, null = True, blank = True)
    calories = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.calories} calories"
