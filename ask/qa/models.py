from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
	title = models.CharField()
	text = models.TextField()
	added_at = models.DateTimeFile()
	rating = models.IntegerField()
	author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
	likes = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)

class Answer(models.Model):
	text = models.models.TextField()
	added_at = models.DateTimeFile()
	question = models.ForeignKey(Question, null=True, on_delete=DO_NOTHING)
	author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
