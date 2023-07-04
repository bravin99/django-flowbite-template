from django.db import models


class NewsletterBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Subscriber(NewsletterBaseModel):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    receive_emails = models.BooleanField(default=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

