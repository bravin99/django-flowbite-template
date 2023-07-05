from django.db import models
from django.utils.text import slugify


class NewsletterBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Subscriber(NewsletterBaseModel):
    confirmation_id = models.CharField(max_length=40)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    receive_emails = models.BooleanField(default=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Newsletter(NewsletterBaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    receivers = models.ManyToManyField(Subscriber, related_name='subscribers')

    def __str__(self):
        return f'{self.title} - {self.created}'

    def save_base(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

