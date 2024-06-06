from django.contrib import admin
from testapp.models import Book,Magagin,NewsPaper


class BookAdmin(admin.ModelAdmin):
    list_display=['title','author','pages','price']
admin.site.register(Book,BookAdmin)
class MagaginAdmin(admin.ModelAdmin):
    list_display=['title','author','publish_date','article']
admin.site.register(Magagin,MagaginAdmin)

class NewPaperAdmin(admin.ModelAdmin):
    list_display=['Name','headline','publish_date']
admin.site.register(NewsPaper,NewPaperAdmin)
# Register your models here.
