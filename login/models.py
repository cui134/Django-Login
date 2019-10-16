# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserInfo(BaseModel):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    user = models.OneToOneField(User)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    # name = models.CharField(max_length=128, unique=True)
    # password = models.CharField(max_length=256)
    # email = models.EmailField(unique=True)
    # sex = models.CharField(max_length=32, choices=gender, default="男")
    # c_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        # 使用__str__方法帮助人性化显示对象信息；
        return self.user.username
    class Meta:
        db_table = "user_info"
        ordering = ["-created_at"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

    @classmethod
    def get_user_by_auth_user_id(cls, _id):
        user = cls.objects.filter(user__id=_id)
        if user.exists():
            return user.first()
        return None