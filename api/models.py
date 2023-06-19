from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    directory = models.CharField(max_length=255)
    important = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
