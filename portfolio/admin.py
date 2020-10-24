from django.contrib import admin
from .models import Data,Category,SlideImage

# Admin page changes

admin.site.site_header = "قسمت مدیریت وبسایت"
admin.site.site_title = "مدیریت وبسایت"

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','parent')
    search_fields = ('title','slug')

admin.site.register(Category, CategoryAdmin)

class DataAdmin(admin.ModelAdmin):
    list_display = ('title','slug','date','author','category_to_str')
    list_filter = ('date','author')
    search_fields = ('title','paragraph')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Data, DataAdmin)

class SlideAdmin(admin.ModelAdmin):
    list_display = ('position',)

admin.site.register(SlideImage,SlideAdmin)
