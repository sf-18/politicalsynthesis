from django.db import models

# Create your models here.
class Candidate(models.Model):
    candidate_photo = models.TextField()
    candidate_name = models.CharField(max_length=100)
    candidate_party = models.CharField(max_length=50)
    candidate_incumbency = models.CharField(max_length=100)