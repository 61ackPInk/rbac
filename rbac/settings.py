"""
Django settings for rbac project.
"""
from pathlib import Path

# 根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# KEY
SECRET_KEY = 'django-insecure-%te9xa=ii3#t!=47ts26631t^*qok$1puz^p)*1l=xx_81!rhp'

DEBUG = True
ALLOWED_HOSTS = []

# APP
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 安装应用
    'rest_framework',
    'corsheaders',  # drf跨域
    'drf_spectacular',  # 接口文档
    'apps.books',
    'apps.com'
]

# 中间件
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# DRF配置
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_RENDERER_CLASSES': (
        'common.custom.json_render.Renderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )

}

# 接口文档配置
SPECTACULAR_SETTINGS = {
    'TITLE': 'Project API',
    'DESCRIPTION': 'Backend Interface Document',
    'VERSION': '1.0.0',
    # 不在 Swagger 文档中显示 /api/schema/
    'SERVE_INCLUDE_SCHEMA': False,

    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
        'filter': True,
        'docExpansion': 'none',
        'displayRequestDuration': True,
    },
}

# 跨域配置
CORS_ALLOW_ALL_ORIGINS = True   # 允许所有跨域请求

# 根路由
ROOT_URLCONF = 'rbac.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rbac.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'dj_db_conn_pool.backends.mysql',
        'NAME': 'rbac',
        'USER': 'root',
        'PASSWORD': '010601',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'POOL_OPTIONS': {
            'POOL_SIZE': 10,
            'MAX_OVERFLOW': 10,
            'RECYCLE': 24 * 60 * 60,
            'TIMEOUT': 30,
        }
    }
}

# Password validation
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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_TZ = True

# 静态资源访问路径(css, js, img)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_ROOT = BASE_DIR / 'file/img'
MEDIA_URL = 'com/img/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
