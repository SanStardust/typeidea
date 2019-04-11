# -*- coding: utf-8 -*-
"""
create_time: 2019/4/11 - 16:04
where: 7教
description: 开发环境配置文件
changed_time: 2019/4/11 - 16:04
"""
__author__ = 'sanqiushu'


from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),   # 这里把../../db.sqlite3 改为 db.sqlite3
    }
}
