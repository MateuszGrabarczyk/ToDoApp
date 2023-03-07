from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    active = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Task_detail", kwargs={"pk": self.pk})
