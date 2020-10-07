from django.db import models

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
    slug = models.SlugField(max_length=100,unique=True,default='',verbose_name="آدرس مقاله")
    title = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    category = models.ManyToManyField(Category,blank=True, verbose_name="دسته بندی", related_name="projects")
    paragraph = models.TextField(default="",verbose_name="محتوا مقاله")
    date = models.DateTimeField(verbose_name="زمان انتشار مقاله")
    postadby = models.CharField(max_length=100,verbose_name="نویسنده")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-date']

    def __str__(self):
        return self.title
