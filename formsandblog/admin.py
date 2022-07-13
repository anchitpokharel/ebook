from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

class Store_contact_us(admin.ModelAdmin):
    readonly_fields = ['your_name', 'your_email', 'your_number', 'subject', 'message', ]
    

admin.site.register(models.Contact_us, Store_contact_us)

@admin.register(models.Category)
class CategoryFrom(admin.ModelAdmin):
    list_display = ['title']
    
@admin.register(models.Author)
class AuthorForm(admin.ModelAdmin):
    list_display = ['title']

@admin.register(models.Blog)
class BlogPage(admin.ModelAdmin):
    list_display = ['title', 'meta_description','author','category', 'image','alt_desc_image','description','slug', 'description','date_created']
    list_select_related = ['category']
    
    # def category_title(self, blog):
    #     return blog.category.title
    
    list_select_related = ['author']
    
    # def author_title(self, blog):
    #     return blog.author.title