from django.contrib import admin
from .models import Post,Student,Contact,Profile,About,work,Cdetail



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date','image')
    list_display_links = ['image','author' ,'title']
    list_display = ('title', 'author', 'pub_date','image')
    list_filter = [ 'pub_date','author','title' ]
    search_fields = ['author','title']


class ContactAdmin(admin.ModelAdmin):
    #     #fields = [ 'pub_date', 'first_name','last_name',' phone','email ','message ' ]
    list_display = ('fname', 'lname')
    list_display = ('fname', 'lname', 'phone','email','message')
    list_filter = [ 'fname','email']
    search_fields = ['fname','lname','email']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','location')
    list_display = ('user','birth_date','email_confirmed', 'location')
    list_filter = [ 'location', 'user' ]
    search_fields = ['location', 'user' ]

class QuestionAdmin(admin.ModelAdmin):
#     #fields = [ 'pub_date', 'first_name','last_name',' phone','email ','message ' ]
    list_display = ('title', 'pub_date')
    list_display = ('title','by', 'pub_date', 'was_published_recently')
    list_filter = [ 'pub_date','by','title' ]
    search_fields = ['by','title','pub_date']


class DeatilsAdmin(admin.ModelAdmin):
#     #fields = [ 'pub_date', 'first_name','last_name',' phone','email ','message ' ]
    list_display = ('phone', 'pub_date')
    list_display = ('phone','email', 'pub_date', 'was_published_recently')
    list_filter = [ 'phone','pub_date','email' ]


class AboutAdmin(admin.ModelAdmin):
#     #fields = [ 'pub_date', 'first_name','last_name',' phone','email ','message ' ]
    list_display = ('major', 'image','cgpa')
    list_display_links = ['image','major','location']
    list_display = ('major', 'image','cgpa','location','date')
    list_filter = [ 'major','location','date' ]
    search_fields = ['University','major','location']



# detail = models.TextField()
#     document = models.FileField(blank = True, null = True )
#     image = models.ImageField(blank = True, null = True)
#     university = models.CharField( max_length = 100,null = True) 
#     major =  models.CharField( max_length = 50 ,null = True)
#     cgpa =  models.CharField( max_length = 20 ,null = True)
#     date = models.DateField(null = True)
#     location = models.CharField( max_length = 100,null = True )
#     online = models.CharField( max_length = 100,null = True )




admin.site.register(Profile,ProfileAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Student)
admin.site.register(Contact,ContactAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Cdetail,DeatilsAdmin)
admin.site.register(work,QuestionAdmin)
