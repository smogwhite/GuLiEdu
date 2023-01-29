from django.db import models
from datetime import datetime
from users.models import UserProfile


# Create your models here.
class UserAsk(models.Model):
    name = models.CharField(max_length=30, verbose_name="姓名")
    phone = models.CharField(max_length=11, verbose_name="手机")
    course = models.CharField(max_length=20, verbose_name="课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Mate:
        verbose_name = '咨询信息'
        verbose_name_plural = verbose_name


class UserLove(models.Model):
    love_man = models.ForeignKey(UserProfile, verbose_name="收藏用户")
    love_id = models.IntegerField(verbose_name="收藏id")
    love_type = models.IntegerField(choices=((1, 'org'),
                                    (2, 'course'),
                                    (3, 'teacher')),
                                    verbose_name="收藏类别"
                                )
    love_state = models.BooleanField(default=False,verbose_name="收藏状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.love_man.username

    class Mate:
        verbose_name = '收藏信息'
        verbose_name_plural = verbose_name
