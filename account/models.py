from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    is_author = models.BooleanField(default=False,verbose_name='وضعیت نویسندگی')
    special_user = models.DateTimeField(default=timezone.now,verbose_name='اشتراک ویژه تا')

    def is_special_user(self):
        if self.is_superuser == False:
            if self.is_author == False:
                if self.special_user > timezone.now():
                    return True
                else:
                    return False
            else:
                return True
        else:
            return True
    is_special_user.boolean = True
    is_special_user.short_description = 'وضعیت کاربر ویژه'