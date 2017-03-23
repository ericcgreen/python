from django.db import models

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)
# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # random = models.CharField(max_length=200)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = EntryQuerySet.as_manager()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name ="Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
