from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.TextField()
    user_age = models.IntegerField()
    user_phone = models.TextField()
    user_address = models.TextField()

    def __str__(self):
        return self.user_name
