from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to="img/")
    created_at = models.DateTimeField(auto_now_add=True)

    projects = models.Manager()
