from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100,unique=True,default='',verbose_name="آدرس دسته بندی")
    parent = models.ForeignKey('self',default=None,null=True,blank=True,on_delete=models.SET_NULL,related_name="children",verbose_name="زیر دسته")
    position = models.IntegerField(verbose_name="جایگاه")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title

class Data(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='projects',verbose_name='نویسنده')
    slug = models.SlugField(max_length=100,unique=True,default='',verbose_name="آدرس مقاله")
    title = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    category = models.ManyToManyField(Category,blank=True, verbose_name="دسته بندی", related_name="projects")
    paragraph = models.TextField(default="",verbose_name="محتوا مقاله")
    date = models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار مقاله")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("account:home")

    def category_to_str(self):
        return " , ".join([category.title for category in self.category.all()])
    category_to_str.short_description = 'دسته بندی'

