from django.db import models

# Create your models here.
class Candidate(models.Model):
    candidate_photo = models.CharField
    candidate_name = models.CharField
    candidate_party = models.CharField