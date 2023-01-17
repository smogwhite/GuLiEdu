from django.db import models


# Create your models here.
class CourseInfo(models.Model):
    image = models.ImageField(upload_to='course/', max_length=200, verbose_name="课程封面")
    name = models.CharField(max_length=20, verbose_name="课程名称")
    study_time = models.IntegerField(default=0, verbose_name="学习时长")
    study_num = models.IntegerField(default=0, verbose_name="学习人数")
    lever = models.CharField(choices=(('gj', '高级'), ('zj', '中级'), ('cj', '初级')),
                             max_length=5, verbose_name="课程难度", default='cj')
    love_num = models.IntegerField(default=0, verbose_name="收藏数")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    desc = models.CharField(max_length=200, verbose_name="课程简介")
    detail = models.TextField(verbose_name="课程详情")
    category = models.CharField(choices=(
        ('qd', '前端开发'), ('hd', '后端开发')
    ), verbose_name="课程类别", max_length=5
    )

