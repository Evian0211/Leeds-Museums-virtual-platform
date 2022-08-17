from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Evaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.CharField(max_length=100)

class Evaluation_quiz_answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    q_number = models.IntegerField()
    answer = models.IntegerField()

class Curriculum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    score = models.FloatField()