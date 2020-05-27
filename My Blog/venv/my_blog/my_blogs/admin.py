from django.contrib import admin

from my_blogs.models import Topic,Entry

admin.site.register(Topic) #通过admin.site.register()来管理我们的模型
admin.site.register(Entry)
