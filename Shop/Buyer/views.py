import hashlib
from Seller.models import User
from django.shortcuts import render, HttpResponseRedirect


def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    result = md5.hexdigest()
    return result


def login_valid(func):
    def inner(request, *args, **kwargs):
        request.COOKIES.get("user_id")
        request.COOKIES.get("username")
        request.session.get("username")
        return func(request, *args, **kwargs)

    return inner


def register(request):
    error_message = ""
    if request.method == "POST":
        username = request.POST.get("user_name")
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        c_password = request.POST.get("cpwd")
        if password == c_password:
            if email:
                user = User.objects.filter(username=username).first()
                if not user:
                    new_user = User()
                    new_user.username = username
                    new_user.email = email
                    new_user.password = password
                    new_user.save()
                    return HttpResponseRedirect("/Buyer/login")
                else:
                    error_message = "用户名已存在"
            else:
                error_message = "请输入邮箱"
        else:
            error_message = "两次密码输入不一致，请重新输入！"

    return render(request, 'buyer/register.html', locals())


def login(request):
    error_message = ""
    username = request.POST.get('user_name')
    password = request.POST.get("pwd")
    if username:
        user = User.objects.filter(username=username).first()
        if user:
            password = set_password(password)
            if password == user.password:
                response = HttpResponseRedirect('/Buyer/index')
                response.set_cookie("username", user.username)
                response.set_cookie("user_id", user.id)
                request.session["username"] = user.username
                return response
            else:
                error_message = "密码错误"
        else:
            error_message = "用户不存在！"
    else:
        error_message = "请输入用户名！"
    return render(request, 'buyer/login.html', locals())


def index(request):
    return render(request, 'buyer/index.html', locals())


def logout(request):
    response = HttpResponseRedirect("/Buyer/login")
    response.delete_cookie("username")
    response.delete_cookie("user_id")
    del request.session["username"]

    return response
