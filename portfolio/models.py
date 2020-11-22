from django.db import models
from account.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment

# My managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


# Create your models here.

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='آدرس آی پی')

    class Meta:
        verbose_name = "آی پی"
        verbose_name_plural = "آی پی ها"

    def __str__(self):
        return self.ip_address

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
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده'),
        ('i', 'در حال بررسی'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="projects", verbose_name='نویسنده')
    slug = models.SlugField(max_length=100,unique=True,default='',verbose_name="آدرس مقاله")
    title = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    category = models.ManyToManyField(Category,blank=True, verbose_name="دسته بندی", related_name="projects")
    paragraph = models.TextField(default="",verbose_name="محتوا مقاله")
    date = models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار مقاله")
    is_special = models.BooleanField(default=False,verbose_name="مقاله ویژه")
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='d',verbose_name="وضعیت")
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress,through='ArticleHit', blank=True, related_name='hits', verbose_name='بازدید ها')

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-date']

    def __str__(self):
        return self.title

    # برای ریدایرکت کردن
    def get_absolute_url(self):
        return reverse("account:home")

    def category_to_str(self):
        return " , ".join([category.title for category in self.category.all()])
    category_to_str.short_description = 'دسته بندی'

    objects = ArticleManager()


class SlideImage(models.Model):
    image = models.ImageField(upload_to='media')
    position = models.IntegerField(unique=True,verbose_name="جایگاه")

    class Meta:
        verbose_name = "اسلاید"
        verbose_name_plural = "اسلاید ها"
        ordering = ['position']

    def image_tag(self):
        return format_html("<img style='width:180px;height:130px;border-radius:10px' src='{}'>".format(self.image.url))
    image_tag.short_description = 'عکس'

class ArticleHit(models.Model):
    article = models.ForeignKey(Data, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)