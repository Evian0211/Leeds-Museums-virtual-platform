from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    got_recommended_item = models.BooleanField(default=False)

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Ticket(models.Model):
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
    course = models.CharField(max_length=100)
    score = models.FloatField()

class Course_quiz_answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    question = models.IntegerField()
    answer = models.IntegerField()