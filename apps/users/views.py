# _*_ encoding:utf-8 _*_

from django.shortcuts import render, HttpResponse, redirect
# django认证方法 authenticate是验证方法, login是登录方法
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
# django的注册密码加密处理
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForGetPwdForm, ModifyPwdForm
from utils.email_send import send_register_email
# Create your views here.


class CustomBackend(ModelBackend):
    """
    重写authenticate方法, 自定义登录用户名
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None



class ForGetPwdView(View):
    '''
    密码找回模块
    '''
    def get(self, request):
        forgetpwd_form = ForGetPwdForm()
        print forgetpwd_form.errors

        return render(request, 'forgetpwd.html', {"forgetpwd_form": forgetpwd_form})

    def post(self, request):
        forgetpwd_form = ForGetPwdForm(request.POST)

        if forgetpwd_form.is_valid():
            email = request.POST.get("email", '')

            if UserProfile.objects.filter(email=email):
                send_email_status = send_register_email(email, "forget")
                if send_email_status:
                    return render(request, 'send_success.html')

            else:
                return render(request, 'forgetpwd.html', {"msg": "此邮箱没有在本网站注册", "forgetpwd_form": forgetpwd_form})
        else:
            return render(request, 'forgetpwd.html', {"forgetpwd_form": forgetpwd_form})



class ResetView(View):
    '''
    密码找回邮箱验证码模块
    '''
    def get(self, request, active_code):
        # 激活码判断
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for records in all_records:
                if records.active_status is False:
                    email = records.email
                    records.active_status = True
                    records.save()
                    return render(request, 'password_reset.html', {'email': email})
                else:
                    return render(request, 'active_fail.html', {'msg':'此验证码已经失效,请重新申请验证码'})
        else:
            return render(request, 'active_fail.html', {'msg':'链接失效或有误'})



class ModifyPwdView(View):
    '''
    密码重置模块
    '''
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')

            if pwd1 == pwd2:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(pwd1)
                user.save()

                return render(request, "login.html")
            else:
                return render(request, "password_reset.html", {"email": email, "msg": '密码不一致'})
        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email": email, 'modify_form': modify_form})



class AcitveUserView(View):
    '''
    邮箱激活用户模块
    '''
    def get(self, request, active_code):
        # 激活码判断
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for records in all_records:
                if records.active_status is False:
                    email = records.email
                    user = UserProfile.objects.get(email=email)
                    user.is_active = True
                    records.active_status = True
                    records.save()
                    user.save()
                    return redirect('/login/')
                else:
                    return render(request, 'active_fail.html', {'msg': '激活码已经使用过，请勿重复使用'})
        else:
            return render(request, 'active_fail.html', {'msg':'链接失效或有误'})



class RegisterView(View):
    """
    用户注册模块
    """
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):

                return render(request, 'register.html', {'register_form': register_form, 'msg': '邮箱已经被注册'})
            else:
                pass_word = request.POST.get("password", "")

                # ORM存储注册用户
                user_profile = UserProfile()
                user_profile.username = user_name
                user_profile.email = user_name
                user_profile.is_active = False
                user_profile.password = make_password(pass_word)
                user_profile.save()
                send_register_email(user_name, "register")

                return render(request, 'active_fail.html', {'msg': '邮件已经发送，请去邮箱里激活账号'})
        else:
            return render(request, 'register.html', {'register_form': register_form})




class LoginView(View):
    """
    用户登录模块
    """
    def get(self, request):

        return render(request, 'login.html', {})

    def post(self, request):

        # form验证
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            # 获取账号密码
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")

            # 如果成功user是一个对象，如果不成功user是none
            user = authenticate(username=user_name, password=pass_word)

            # 如果登陆成功就开始执行登录动作
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {"msg": "账号未激活!"})
            else:
                return render(request, 'login.html', {"msg": "用户名或密码错误!"})
        else:
            return render(request, 'login.html', {'login_form':login_form})



