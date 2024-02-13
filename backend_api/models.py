from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    links = models.CharField(max_length=1000)
    # user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
