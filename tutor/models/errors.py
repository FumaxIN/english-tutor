import uuid
from django.db import models
from django.utils.timezone import now

from .users import User
from .enums import SuperBucket


class Error(models.Model):
    id = uuid.uuid4()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    errorCategory = models.IntegerField(choices=SuperBucket.choices)
    errorSubCategory = models.IntegerField()
    timestamp_utc = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user} - {self.errorCategory} | {self.errorSubCategory} | {self.timestamp_utc}"

    class Meta:
        verbose_name_plural = "Errors"
        ordering = ["-timestamp_utc"]