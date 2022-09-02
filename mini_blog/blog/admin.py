from django.contrib import admin
from .models import Blog_Post
from blog.models import Contact
# Register your models here.
@admin.register(Blog_Post )
class PostModelAdmin(admin.ModelAdmin):
 list_display =["id" , 'title', "desc"]


class ContactAdmin(admin.ModelAdmin):
 list_display =["name" , 'email', "address" ,"desc", "date"]
admin.site.register(Contact, ContactAdmin)

