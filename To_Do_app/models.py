from django.db import models


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    accepted = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def __str__(self):
        return f"{self.content}({self.datetime}): {self.accepted}"

    class Meta:
        ordering = ["accepted", "-datetime"]


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name