from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django .db .models.signals import post_save
from django.dispatch import receiver



class Post (models.Model):
    body =models.TextField()
    image=models.ImageField(upload_to='uploads/post_photo',blank=True,null=True)
    date_on=models.DateTimeField( default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,blank=True,related_name='like')
    dislikes=models.ManyToManyField(User,blank=True,related_name='dislike')
    
    
class Comment(models.Model):
    comment =models.TextField()
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    date_on=models.DateTimeField( default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,blank=True,related_name='likecomment')
    dislikes=models.ManyToManyField(User,blank=True,related_name='dislikecomment')
    parent=models.ForeignKey('self',on_delete=models.CASCADE ,blank=True,null=True,related_name='+')
    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by("-date_on").all()
    @property
    def is_parent(self):
        if self.parent is None :
            return True
        else :
            return False




class UserProfile(models.Model):
      user=models.OneToOneField(User,primary_key=True,verbose_name='user',related_name='profile',on_delete=models.CASCADE)
      name =models.CharField(max_length=100,blank=True,null=True)
      bio=models.TextField(max_length=500,blank=True,null=True)
      birth_date=models.DateField(max_length=500,blank=True,null=True)
      location=models.CharField(max_length=100,blank=True,null=True)
      picture=models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png',blank=True,null=True)
      followers=models.ManyToManyField(User,blank=True, related_name='followers')
      

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
@receiver(post_save, sender=User) 
def save_user_profile(sender,instance,**kwargs):  
    instance.profile.save()  
    

class Notifications(models.Model):
    # 1like   2 comment 3 follow  4 message 
    notification_type=models.IntegerField()
    to_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='notifications_to')
    from_user=models.ForeignKey(User,on_delete=models.CASCADE ,related_name="notifications_from")
    post=models.ForeignKey(Post,related_name="notifications_post", on_delete=models.CASCADE,blank=True,null=True)
    comment=models.ForeignKey(Comment,related_name="notifications_comment", on_delete=models.CASCADE,blank=True,null=True)
    thread=models.ForeignKey('ThreadModel',on_delete=models.CASCADE,related_name='threadnot',null=True,blank=True)
    date_on=models.DateTimeField( default=timezone.now)
    user_has_seen=models.BooleanField(default=False)

class ThreadModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='threaduser')
    receiver=models.ForeignKey(User,  on_delete=models.CASCADE,related_name='threadreceiver')
class MessageModel(models.Model):
    thread=models.ForeignKey('ThreadModel',on_delete=models.CASCADE,related_name='thread')
    sender_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender_user') 
    receiver_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver_user') 
    body=models.TextField(max_length=1000) 
    image=models.ImageField(upload_to='uploads/message_photo' ,blank=True,null=True) 
    date_on=models.DateTimeField( default=timezone.now)
    is_read=models.BooleanField(default=False)