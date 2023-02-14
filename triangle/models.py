from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.first_name



class LoggerModel(models.Model):
    path = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    host = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    data = models.JSONField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.path