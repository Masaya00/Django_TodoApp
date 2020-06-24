from django.db import models
from django.views.generic import ListView
# Create your models here.


PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))
class TodoModel(models.Model):
    title = models.CharField(max_length=50)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY
    )
    duedate = models.DateTimeField()

    def __str__(self):
        return self.title



