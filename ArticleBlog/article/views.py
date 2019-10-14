from django.shortcuts import render


def index(request):
    return render(request, "index.html", locals())


def person_info(request):
    return render(request, "person_info.html", locals())


def photos(request):
    return render(request, 'photos.html', locals())


def diaries(request):
    return render(request, 'diaries.html', locals())
