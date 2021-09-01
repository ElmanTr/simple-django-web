#from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FieldsMixin, FormValidMixin, AuthorAccessMixin, SuperUserAccessMixin, AuthorsUserAccessMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from portfolio.models import Data
from django.urls import reverse_lazy
from .models import User
from .forms import ProfileForms, SignupForm
from django.contrib.auth.views import LoginView, PasswordChangeView

# Create your views here.

class ArticleList(AuthorsUserAccessMixin,ListView):
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Data.objects.all()
        else:
            return Data.objects.filter(author=self.request.user)

class ArticleCreate(AuthorsUserAccessMixin,FormValidMixin,FieldsMixin,CreateView):
    model = Data
    template_name = "registration/article-create-update.html"

class ArticleUpdate(AuthorAccessMixin,FormValidMixin,FieldsMixin,UpdateView):
    model = Data
    template_name = "registration/article-create-update.html"

class ArticleDelete(SuperUserAccessMixin,DeleteView):
    model = Data
    success_url = reverse_lazy('account:home')
    template_name = "registration/confirm_delete.html"

class Profile(LoginRequiredMixin,UpdateView):
    model = User
    template_name = "registration/profile.html"
    success_url = reverse_lazy('account:profile')
    form_class = ProfileForms

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class Login(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_superuser or user.is_author:
            return reverse_lazy("account:home")
        else:
            return reverse_lazy("account:profile")

class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy("password_change_done")



from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import login

class Registration(CreateView):
    form_class = SignupForm
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعالسازی اکانت'
        message = render_to_string('registration/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse("""
        <html dir="rtl" lang='fa'>
        <center>
        <h2 class='my font'>لینک فعالسازی به ایمیل شما ارسال شد!</h2>
        <a style='text-decoration:none' href="..">برگشت به صفحه اصلی</a>
        </center>
        </html>
        """)

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your blog account.'
#             message = render_to_string('acc_active_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token':account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(
#                         mail_subject, message, to=[to_email]
#             )
#             email.send()
#             return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('اکانت شما با موفقیت فعال شد!')
    else:
        return HttpResponse('لینک فعالسازی منقضی شده است!')