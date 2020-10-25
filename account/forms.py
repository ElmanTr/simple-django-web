from django import forms
from .models import User

class ProfileForms(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super(ProfileForms, self).__init__(*args,**kwargs)

        self.fields['username'].help_text = 'الزامی. 150 کاراکتر یا کمتر. فقط شامل حروف، اعداد، و علامات @/./+/-/_'
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
        ]