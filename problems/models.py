from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    name = models.CharField(max_length=300)

    def save(self, *args, **kwargs) -> None:
        self.name = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Problem(models.Model):
    title = models.CharField(max_length=255, validators=[
                             MinLengthValidator(limit_value=5,
                                                message="The problem's title cannot be shorter than 5 characters.")])
    body = models.TextField(validators=[MinLengthValidator(limit_value=10,
                                                           message="The problem's body cannot be shorter than 10 characters.")])
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='problems')
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title
