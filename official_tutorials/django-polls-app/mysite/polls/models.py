import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        """Define string representation for object, i.e. when using manage.py shell."""
        return self.question_text

    ## Use the @admin decorator to control how this method displays in the admin site
    @admin.display(boolean=True, ordering="pub_date", description="Published recently?")
    def was_published_recently(self) -> bool:
        """Return True if Questions' .pub_date is within the last 1 day."""
        now = timezone.now()

        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        """Define string representation for object, i.e. when using manage.py shell."""
        return self.choice_text
