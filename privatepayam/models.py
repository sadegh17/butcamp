from django.db import models
from django.conf import settings



# Create your models here.
User = settings.AUTH_USER_MODEL

class Private(models.Model):
    owner   =models.ForeignKey(User , on_delete=models.CASCADE, related_name="saheb")
    dest    =models.ForeignKey(User , on_delete=models.CASCADE,related_name="maghsad")
    matn    =models.TextField(max_length=250)
    read    =models.BooleanField(default=False)
    time        =models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.owner.username
