from django.db import models
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, related_name='questions')
    title = models.CharField(max_length=240)
    description = models.TextField()
    tags = TaggableManager()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('questions:single',kwargs={'username':self.user.username, 'pk':self.pk})

    class Meta:
        ordering = ['-created_at']

    def get_answers(self):
        return Answer.objects.filter(question=self)

    def get_answers_count(self):
        return Answer.objects.filter(question=self).count()



class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    votes = models.IntegerField(default=0)
    is_accepted = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ('-votes','created_at')

    def __str__(self):
        return self.description
