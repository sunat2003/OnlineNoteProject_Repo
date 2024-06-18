from django.contrib import admin
from testapp.models import Topic
# Register your models here.
class TopicAdmin(admin.ModelAdmin):
     list_display=['topic','subject']


admin.site.register(Topic,TopicAdmin)
    
