from django.db import models
from django.contrib.auth.hashers import make_password


class user(models.Model):
    uid = models.IntegerField(primary_key = True,auto_created = True)
    uname = models.CharField(max_length=30,default="Default")
    about = models.CharField(max_length=30,default="Available")
    pphoto = models.ImageField(default='defaultprofile.jpg')
    phoneno = models.CharField(max_length=13)


class message(models.Model):
    uid1 = models.ForeignKey(user, on_delete=models.CASCADE,related_name="message_sender")
    uid2 = models.ForeignKey(user, on_delete=models.CASCADE,related_name="message_reciever")
    message = models.TextField()


class feedback(models.Model):
    uid1 = models.ForeignKey(user, on_delete=models.CASCADE,related_name="sender")
    feedbackmsg = models.TextField()


class admin2(models.Model):
    uid1 = models.ForeignKey(user,default=1,on_delete=models.CASCADE,related_name="admin")
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

