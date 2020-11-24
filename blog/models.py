from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_text
