from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
