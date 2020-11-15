from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractUser):
    is_author = models.BooleanField(default=False,verbose_name='وضعیت نویسندگی')
    special_user = models.DateTimeField(default=timezone.now,verbose_name='اشتراک ویژه تا')
    photo = models.ImageField(upload_to="profileimg",blank=True, verbose_name='عکس')

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

    def clean(self):
        for char in self.username:
            if char in ['ض','ص','ث','ق','ف','غ','ع','ه','خ','ح','ج','چ','ش','س','ی','ب','ل','ا','ت','ن','م','ک','گ','پ','ظ','ط','ز','ر','ذ','د','ئ','و','ً','ٍ','ٌ','َ','ُ','ِ','ّ','ۀ','آ','»','«','"','|',':','،','؛',',',']','[','{','}','ة','ي','ژ','إ','ؤ','أ','ء','<','>','؟','!','#','%','^','&','*',')','=','÷','×','/',';',"'",',','?','$']:
                raise ValidationError("نام کاربری باید 150 کاراکتر یا کمتر، فقط شامل حروف انگلیسی، اعداد و علامات @/./+/-/_  باشد")