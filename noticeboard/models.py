from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
