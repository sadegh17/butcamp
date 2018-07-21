from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save ,post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from django.urls import reverse

# Create your models here.
User = settings.AUTH_USER_MODEL
class Users (models.Model):

    user        = models.OneToOneField(User ,on_delete=models.CASCADE)
    follower    = models.ManyToManyField(User , related_name="is_follow" , blank=True)
    name        = models.CharField(max_length=120)
    email       = models.EmailField(blank=True,null=True)
    myfave      = models.TextField(help_text='seprate your fave by coma')
    color       = models.CharField(max_length=120 , default="a80000" ,help_text='give me a hex color number to set :)')
    timeadd     = models.DateTimeField(auto_now_add=True)
    timeup      = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(null=True,blank=True)

    def get_fave(self):
        return self.myfave.split(",")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Users, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("update" , kwargs={"slug":self.slug})

    def __str__(self):
        return self.user.username

# def fr_pre_save_rec(sender , instance,*args,**kwargs):
# 	if not instance.slug:
# 		instance.slug = instance.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(user=instance)
    instance.users.save()


 # pre_save.connect(fr_pre_save_rec , sender=user)
# post_save.connect(post_save_user , sender=Users)
