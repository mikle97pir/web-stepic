from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=191, null=True, default='')
    text = models.TextField(null=True, default='')
    added_at = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(default=0, null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='question_like_user')
    def __str__(self):
        return self.title
    def get_url(self):
        return reverse('question-id', kwargs={'id': self.id})

class Answer(models.Model):
    text = models.TextField(null=True, default='')
    added_at = models.DateTimeField(auto_now_add=True, null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.text