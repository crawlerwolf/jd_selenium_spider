# -*- coding: utf-8 -*-
# author = minjie
from peewee import *

db = MySQLDatabase(
    database='test',
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root'
    )


class BaseModel(Model):
    class Meta:
        database = db


class Good(BaseModel):
    """商品信息"""
    id = IntegerField(primary_key=True, verbose_name="商品id")
    name = CharField(max_length=500, verbose_name="商品名称")
    price = FloatField(default=0.0, verbose_name="商品价格")
    content = TextField(default="", verbose_name="商品描述")
    supplier = CharField(default="", max_length=500, verbose_name="供货商")
    ggbz = TextField(default="", verbose_name="规格和包装")
    image_list = TextField(default="", verbose_name="商品展示图")

    good_rate = IntegerField(default=0, verbose_name="好评率")
    comments_nums = IntegerField(default=0, verbose_name="评论数")
    has_image_comment_nums = IntegerField(default=0, verbose_name="晒图数")
    has_video_comment_nums = IntegerField(default=0, verbose_name="视频晒单数")
    has_add_comment_nums = IntegerField(default=0, verbose_name="追评数")
    well_comment_nums = IntegerField(default=0, verbose_name="好评数")
    middle_comment_nums = IntegerField(default=0, verbose_name="中评数")
    bad_comment_nums = IntegerField(default=0, verbose_name="差评数")


class GoodEvaluate(BaseModel):
    """商品评价"""
    id = CharField(primary_key=True,  verbose_name="用户id")
    good = ForeignKeyField(Good, verbose_name="商品")
    user_head_url = CharField(verbose_name="用户头像")
    user_name = CharField(verbose_name="用户名")
    good_info = CharField(default="", max_length=500, verbose_name="购买商品的信息")
    evaluate_time = DateTimeField(verbose_name="评价时间")
    content = TextField(default="", verbose_name="评价内容")
    star = IntegerField(default=0, verbose_name="评分")
    comment_nums = IntegerField(default=0, verbose_name="评论数")
    praised_nums = IntegerField(default=0, verbose_name="点赞数")
    image_list = TextField(default="", verbose_name="评价图片")
    video_list = TextField(default="", verbose_name="评价视频")


class GoodEvaluateSummary(BaseModel):
    """评价标签"""
    good = ForeignKeyField(Good, verbose_name="商品")
    tag = CharField(default="", max_length=20, verbose_name="标签")
    num = IntegerField(default=0, verbose_name="数量")


if __name__ == "__main__":
    db.create_tables([Good, GoodEvaluate, GoodEvaluateSummary])
