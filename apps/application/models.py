from django.db import models
from ..registration.models import User


class Application(models.Model):
    github_username = models.CharField(max_length=39, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "({}) {}".format(self.id, self.user.email)


class Question(models.Model):
    text = models.TextField()
    type = models.CharField(max_length=255)


class Answer(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()