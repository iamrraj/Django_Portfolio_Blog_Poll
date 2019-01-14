from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe
from django.utils import timezone
import datetime

from markdown_deux import markdown


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    body = models.TextField()
    description = models.TextField(null=True)
    pub_date = models.DateField()
    image = models.ImageField(null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def get_markdown(self):
        description = self.description
        markdown_text = markdown(description)
        return mark_safe()



class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Contact(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()



    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    image = models.ImageField(blank = True, null = True )

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class work(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank = True, null = True)
    by = models.CharField(max_length=50)
    pub_date = models.DateTimeField( 'date published' )

    def __str__( self ):
        return self.title

    def __unicode__(self):
        return self.title




    def was_published_recently( self ):
        now = timezone.now()
        return now - datetime.timedelta( days = 1 ) <= self.pub_date <= now


class About(models.Model):
    detail = models.TextField()
    document = models.FileField(blank = True, null = True )
    image = models.ImageField(blank = True, null = True)
    university = models.CharField( max_length = 100,null = True) 
    major =  models.CharField( max_length = 50 ,null = True)
    cgpa =  models.CharField( max_length = 20 ,null = True)
    date = models.DateField(null = True)
    location = models.CharField( max_length = 100,null = True )
    online = models.CharField( max_length = 100,null = True )


    def __str__( self ):
        return self.detail



class Cdetail(models.Model):
    phone = models.CharField( max_length = 30 )
    email = models.EmailField()
    address = models.TextField()
    pub_date = models.DateTimeField( 'date published' )

    def __str__( self ):
        return self.phone

    def was_published_recently( self ):
        now = timezone.now()
        return now - datetime.timedelta( days = 1 ) <= self.pub_date <= now

