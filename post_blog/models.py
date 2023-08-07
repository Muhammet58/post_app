from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class post_model(models.Model):
    author = models
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(db_index=True, blank=True,)


    class Meta:
        ordering = ["-publish_date"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

