from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class CustomUser(User):
    def __str__(self) -> str:
        return f'Name: {self.username}, email: {self.email}'
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    