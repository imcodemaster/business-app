from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from accounts.forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView

from django.contrib.auth.forms import AuthenticationForm
from validate_email import validate_email
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from accounts.utils import account_activation_token
from django.contrib import messages
#from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.views import View
from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from django.views.generic import View
from django.utils import timezone
from django.contrib import auth

from urllib.parse import urlparse, urlunparse

from django.conf import settings
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import (
    url_has_allowed_host_and_scheme, urlsafe_base64_decode,
)
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .render import Render
from django.contrib.auth.models import User 
from .models import Profile
# Create your views here.


class Register(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = '../templates/accounts/register.html'

    def form_valid(self,form):
        user = form.save()
        email = form.data.get('email')
        current_site = get_current_site(self.request)
        email_body = {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            }

        link = reverse('activate', kwargs={
                                'uidb64': email_body['uid'], 'token': email_body['token']})
        email_subject = 'Activate your account'
        activate_url = 'http://' + current_site.domain + link
        email = EmailMessage(
            email_subject,
            'Hello ' + user.username + ', Please click on the link below to activate your account \n' + activate_url,
             'sharma.mohan57698@gmail.com',[email],)
        print(email)
        email.send(fail_silently=True)
        return redirect('emaiverify')


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'sorry email in use,choose another one '}, status=409)
        return JsonResponse({'email_valid': True})





def emaiverify(request):
    return render(request,'../templates/accounts/emaiverify.html')



class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()
            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass

        return redirect('login')    

@login_required
def ProfileView(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST , instance= request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'your profile is updated')
            return redirect('home')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance= request.user.profile)

    context  = {
    'u_form': u_form,
    'p_form': p_form
    }

    return render(request,'../templates/accounts/profile.html', context)



class identitycardView(View):

    def get(self, request):
        getpdf = Profile.objects.filter(user = request.user)
        today = timezone.now()
    
        params = {
            'today': today,
            'getpdf': getpdf,
            'request': request
            }
        return Render.render( '../templates/accounts/profile_pdf.html',  params)    
