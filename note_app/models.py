from django.db import models

# Create your models here.
class signup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    city = models.CharField(max_length=20)
    mobile = models.BigIntegerField()

class notes(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=200)
    option=models.CharField(max_length=100)
    file=models.FileField(upload_to='MyNotes')
    comment=models.TextField()


class feedback(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()
    msg=models.TextField()