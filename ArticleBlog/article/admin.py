from django.contrib import admin
from article.models import *

admin.site.register(Author)
admin.site.register(ArticleType)
admin.site.register(Article)
