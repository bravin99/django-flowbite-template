from django.db import models


class MainAppBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Contact(MainAppBaseModel):
    full_name = models.CharField(max_length=65)
    email = models.EmailField()
    phone = models.CharField(max_length=13, null=True, blank=True)
    message = models.TextField()
    call_back = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.full_name}: {self.created}"

    class Meta:
        ordering = ('-created',)

