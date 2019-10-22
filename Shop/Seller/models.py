from django.db import models


# 用户表：用户名,邮箱，密码，手机号，照片，地址，用户类型（买家0，卖家1）
class User(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    user_phone = models.CharField(max_length=32)
    user_image = models.ImageField(upload_to="seller/images", default="seller/images/1.png")
    user_address = models.TextField()
    user_type = models.IntegerField(default=0)


# 商品类型表
class GoodsType(models.Model):
    type_label = models.CharField(max_length=32)
    type_description = models.TextField()


# 商品表 商品编号，商品名称，商品描述，商品图片，商品数量，商品价格，生产日期，保质期，商品类型
class Goods(models.Model):
    goods_number = models.CharField(max_length=32)
    good_name = models.CharField(max_length=32)
    goods_description = models.TextField()
    goods_price = models.FloatField()
    goods_content = models.IntegerField()
    goods_pub_time = models.DateField(auto_now=True)
    goods_shelf_life = models.IntegerField()
    goods_type = models.ForeignKey(to=GoodsType, on_delete=models.CASCADE)
