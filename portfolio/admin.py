from django.contrib import admin
from .models import Data, Category, SlideImage, IPAddress

# Admin page changes

admin.site.site_header = "قسمت مدیریت وبسایت"
admin.site.site_title = "مدیریت وبسایت"

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title_fa', 'slug', 'parent')
    search_fields = ('title_fa','slug')

admin.site.register(Category, CategoryAdmin)

class DataAdmin(admin.ModelAdmin):
    list_display = ('title_fa', 'slug', 'date', 'author', 'category_to_str', 'is_special', 'status')
    list_filter = ('date','author')
    search_fields = ('title_fa','paragraph_fa')
    prepopulated_fields = {'slug':('title_fa',)}

admin.site.register(Data, DataAdmin)

class SlideAdmin(admin.ModelAdmin):
    list_display = ('position','image_tag')

admin.site.register(SlideImage,SlideAdmin)

admin.site.register(IPAddress)