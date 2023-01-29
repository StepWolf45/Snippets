from django.contrib.auth.models import User
from django.db import models


class Snippet(models.Model):
    name = models.CharField(max_length=200)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                             blank=True, null=True)  # can be empty due to usage of AnonymousUser
