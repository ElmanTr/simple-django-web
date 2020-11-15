from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError

class ProfileForms(forms.ModelForm):
        
    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super(ProfileForms, self).__init__(*args,**kwargs)

        self.fields['username'].help_text = 'الزامی. 150 کاراکتر یا کمتر. فقط شامل حروف انگلیسی، اعداد و علامات @/./+/-/_'
        self.fields['photo'].help_text = 'با کلیک یا کشیدن و رها کردن عکس در باکس سبز عکس پروفایل خود را آپلود کنید!'
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True
            self.fields['is_author'].disabled = True
            self.fields['special_user'].disabled = True

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'last_name',
            'first_name',
            'special_user',
            'is_author',
            'photo',
        ]

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=200, required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("این ایمیل قبلا ثبت شده است!")
        return email

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            ]