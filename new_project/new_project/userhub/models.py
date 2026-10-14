from django.db import models


class User(models.Model):

  
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    role = models.CharField(max_length=50)


    class Meta:
        db_table = 'users'
        managed = False

    def __str__(self):
        return self.name

  

