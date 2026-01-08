from django.db import models
from cats.models import SpyCat

class Mission(models.Model):
    cat = models.OneToOneField(
        SpyCat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Mission #{self.id} - Cat: {self.cat.name if self.cat else 'Unassigned'}"

class Target(models.Model):
    mission = models.ForeignKey(
        Mission,
        related_name="targets",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({'Completed' if self.is_completed else 'Pending'})"
