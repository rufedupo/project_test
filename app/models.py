from django.db import models
from datetime import datetime
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def formatted_created_at(self):
        local_timezone = timezone.get_current_timezone()
        local_created_at = self.created_at.astimezone(local_timezone)
        return local_created_at.strftime("%d/%m/%Y %H:%M:%S")
    
    def __str__(self):
        return self.name