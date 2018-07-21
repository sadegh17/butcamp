from django.db import models
from django.conf import settings

user = settings.AUTH_USER_MODEL

# Create your models here.
class Payam(models.Model):
    owner       =models.ForeignKey(user , on_delete=models.CASCADE)
    message     =models.CharField(max_length=250 ,blank=True,null=True)
    time        =models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.owner.username
