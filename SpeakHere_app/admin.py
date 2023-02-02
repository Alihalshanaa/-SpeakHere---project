from django.contrib import admin
from .models import Post ,UserProfile,Comment ,Notifications



admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Notifications)
