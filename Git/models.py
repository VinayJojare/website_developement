from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.name}"
    

    class Meta:
        db_table = "User"




