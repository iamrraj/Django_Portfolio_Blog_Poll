from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date','image')
    list_display_links = ['image','author' ,'title']
    list_display = ('title', 'author', 'pub_date','image')
    list_filter = [ 'pub_date','author','title' ]
    search_fields = ['author','title']


admin.site.register(Post,PostAdmin)
