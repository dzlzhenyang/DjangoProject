import random
import hashlib
from django.shortcuts import render, HttpResponseRedirect
from Seller.models import *


def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    result = md5.hexdigest()
    return result


def login_valid(func):
    def inner(request, *args, **kwargs):
        cookie_email = request.COOKIES.get("email")
        session_email = request.session.get("email")
        if cookie_email and session_email and cookie_email == session_email:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/Seller/login")

    return inner


def register(request):
    error_message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        r_password = request.POST.get("r_password")
        if password == r_password:
            if email:
                user = User.objects.filter(email=email).first()
                if not user:
                    new_user = User()
                    new_user.username = username
                    new_user.email = email
                    new_user.password = set_password(password)
                    # 卖家类型为1
                    new_user.user_type = 1
                    new_user.save()

                    return HttpResponseRedirect("/Seller/login")
                else:
                    error_message = "邮箱已被注册！"
            else:
                error_message = "邮箱不能为空！"
        else:
            error_message = "两次密码输入不一致"

    return render(request, 'seller/register.html', locals())


def login(request):
    error_message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email:
            user = User.objects.filter(email=email).first()
            if user:
                if user.user_type == 1:
                    db_password = user.password
                    password = set_password(password)
                    if db_password == password:
                        # 设置cookie和session
                        response = HttpResponseRedirect("/Seller/index")
                        response.set_cookie("email", user.email)
                        response.set_cookie("user_id", user.id)
                        request.session["email"] = user.email
                        return response
                    else:
                        error_message = "您的权限不够，无法登陆到卖家后台！"
                else:
                    error_message = "密码输入错误，请重新输入！"
            else:
                error_message = "用户不存在"
        else:
            error_message = "请输入邮箱！"
    return render(request, 'seller/login.html', locals())


def logout(request):
    response = HttpResponseRedirect("/Seller/login")
    response.delete_cookie("email")
    response.delete_cookie("uer_id")
    del request.session["email"]

    return response


@login_valid
def index(request):
    return render(request, "seller/index.html", locals())


# 生成6位随机的验证码
def create_code(length=6):
    str1 = "".join(map(chr, range(ord("a"), ord("z") + 1))) + "".join(
        map(chr, range(ord("A"), ord("Z") + 1))) + "1234567890"
    code = ""
    for i in range(length + 1):
        i = random.choice(str1)
        code += i
    return code


# 保存验证码


def send_code(request):
    pass
