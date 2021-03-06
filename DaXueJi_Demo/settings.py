"""
Django settings for DaXueJi_Demo project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3*j!k(4&3j+zmk)hxko1%$nklp^y@gq=ec=9n--^ulc=xd774o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost ', '.sunmouren.xin']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third apps
    'mptt',
    'pure_pagination',
    'notifications',
    'rest_framework',
    # my apps
    'users',
    'writing',
    'topics',
    'actions',
    'comments',
    'private_messages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DaXueJi_Demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 添加图片处理器，使用图片时前面加上MEDIA_URL 例如：{{ MEDIA_URL}}{{ fo.avatar }}
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'DaXueJi_Demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'daxueji',        #数据库名字
        'USER': 'root',          #账号
        'PASSWORD': '12345678',      #密码
        'HOST': '127.0.0.1',    #IP
        'PORT': '3306',                   #端口
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB,character_set_connection=utf8,collation_connection=utf8_unicode_ci;'
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'


# 引入静态文件
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# my settings
LOGIN_URL = '/user/login/'
# 自定义User时
AUTH_USER_MODEL = 'users.UserProfile'
# mask package 为 源/根 时
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# 设置上传文件的路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 增加邮箱登入
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

# qq POP3/SMTP 配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.qq.com"  # SMTP服务器主机
EMAIL_PORT = 465             # 端口
EMAIL_HOST_USER = "2826573494@qq.com"       # 邮箱地址
EMAIL_HOST_PASSWORD = "nldauvwchhdjdccc"    # 密码
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_FROM = "2826573494@qq.com"            # 邮箱地址

# 分页一些配置
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 10,
    'MARGIN_PAGES_DISPLAYED': 2,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

# rest_framework settings
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# 微博登录
WEIBO_APP_ID = "2003416765"
WEIBO_APP_KEY = "2702c87e3527d7c914e64c4d7fd069b0"
WEIBO_REDIRECT_URI = "http://www.sunmouren.xin/user/weibo/login/"



