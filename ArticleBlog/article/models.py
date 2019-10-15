from django.db import models


# 姓名，年龄，性别，出生日期，邮箱，手机号，图片，
class Author(models.Model):
    __tablename__ = "author"
    author_name = models.CharField(max_length=32)
    author_age = models.IntegerField()
    # DateField 年月日  DateTimeField：年月日时分秒
    author_birthday = models.DateField()
    author_gender = models.CharField(max_length=32)
    author_email = models.EmailField()
    author_phone = models.CharField(max_length=32)
    author_photo = models.ImageField(upload_to="images")

    # 返回对应的实例对象名字
    def __str__(self):
        return self.author_name


# 名字，描述
class ArticleType(models.Model):
    __tablename = "article_type"
    type_name = models.CharField(max_length=32)
    type_description = models.TextField()

    def __str__(self):
        return self.type_name


# 标题，类型，作者，描述，内容，出版时间，图片，
class Article(models.Model):
    __tablename__ = "article"
    article_title = models.CharField(max_length=32)
    # 级联删除
    article_type = models.ForeignKey(to=ArticleType, on_delete=models.CASCADE)
    article_author = models.ManyToManyField(to=Author)
    article_description = models.TextField()
    article_content = models.TextField()
    article_pub_time = models.DateField()
    article_image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.article_title
