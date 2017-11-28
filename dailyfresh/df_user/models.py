from django.db import models

# Create your models here.
from db.base_model import BaseModel


class PassportManager(models.Manager):
    '''用户账户模型管理器类'''
    pass


class Passport(BaseModel):
    '''用户账户类'''
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=40, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')
    is_active = models.BooleanField(default=False, verbose_name='激活标记')

    objects = PassportManager()

    class Meta:
        db_table = 's_user_account'  # 重命名数据库
