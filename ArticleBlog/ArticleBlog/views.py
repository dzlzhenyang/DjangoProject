from django.http import HttpResponse


def example(request, name, age):
    return HttpResponse("<h1 style='color:red;'>hello world ,I am %s,I am %s years old </h1>" % (name, age))
