from pathlib import Path
import os
import environ

from django.utils.translation import ugettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_NAME = os.path.basename(BASE_DIR)
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

env = environ.Env()

IS_ON_HEROKU = env.bool('ON_HEROKU', default=False)

if not IS_ON_HEROKU:
    env.read_env(os.path.join(BASE_DIR,'.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env.get_value('DEBUG', cast = bool)

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['portfolio-kf.herokuapp.com','https://portfolio-kf.herokuapp.com/']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'app1.urls' #プロジェクト名をxxxに入れる

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], #htmlなどを格納するフォルダ
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

WSGI_APPLICATION = 'app1.wsgi.application' #プロジェクト名をxxxに入れる


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 追記
import dj_database_url
db_from_env = dj_database_url.config()
if not DEBUG:
    DATABASES['default'].update(db_from_env)




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Core URL settings
# ログイン機能がある場合はコメントアウトを外す
# LOGIN_REDIRECT_URL = 'account:index' #ログイン後のダッシュボード
# LOGIN_URL = 'account:login'
# LOGOUT_REDIRECT_URL = 'account:login'


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

# 英語対応の場合は 下記コメントアウトを外す
LANGUAGES = [
    ('ja', _('日本語')),
    # ('en', _('English')),
]

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and Media files
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/') # 追記
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'


# Upload Settings

DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000
FILE_UPLOAD_MAX_MEMORY_SIZE = 15728640
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640

if not DEBUG:
    import django_heroku
    django_heroku.settings(locals())