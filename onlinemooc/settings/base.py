"""
Django settings for onlinemooc project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mlol_o-+fk#q@^!p-#yeppbu0cq-e6v36trv!&qvlrb=1@%%yx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_api',
    'rest_framework',
    'django_filters',
    'captcha',
    'tyadmin_api_cli',
    'tyadmin_api'
]

AUTH_USER_MODEL = "app_api.User"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'onlinemooc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'onlinemooc.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

try:
    var = os.environ["not_use_docker"]
    UseDocker = False
except KeyError:
    UseDocker = True

if UseDocker:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'online_mooc',  # 数据库名
            'USER': 'root',  # 用户名
            'PASSWORD': 'mtianyanroot',  # 密码
            'HOST': 'mysql',  # 链接id ,空为本地,可以设置绝对路径
            'PORT': '3306',  # 端口号
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'online_mooc',  # 数据库名
            'USER': 'root',  # 用户名
            'PASSWORD': 'mtianyanroot',  # 密码
            'HOST': '127.0.0.1',  # 链接id ,空为本地,可以设置绝对路径
            'PORT': '3306',  # 端口号
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# 语言改为中文
LANGUAGE_CODE = 'zh-hans'

# 时区改为上海
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# 数据库存储使用时间，True时间会被存为UTC的时间
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
REST_FRAMEWORK = {
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    # 使用Django Filter 过滤器
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend', 'rest_framework.filters.SearchFilter'),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'onlinemooc.no_csrf.CsrfExemptSessionAuthentication'
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'onlinemooc.pagination.CustomPageNumberPagination',
    'PAGE_SIZE': 10,
    'ORDERING_PARAM': 'sort',
    'EXCEPTION_HANDLER': 'onlinemooc.custom_exception.custom_exception_handler',
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_HOST = "smtp.qq.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "1147727180@qq.com"
EMAIL_HOST_PASSWORD = "tuzosukurdpjihda"
EMAIL_USE_TLS = True
EMAIL_FROM = "1147727180@qq.com"
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TY_ADMIN_CONFIG = {
    'GEN_APPS': ['app_api']
}
