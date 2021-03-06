"""
Django settings for baitulilm project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#gb7a&o=xk0kb)2t$1o$@%4wtihcgc4t+wfgmebsyp=yo_)67+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django_comments',
    'mptt',
    'tagging',
    'taggit',
    # 'zinnia_bootstrap',
    'ckeditor',
    'ckeditor_uploader',
    # 'zinnia',
    'sorl.thumbnail',
    # 'zinnia_ckeditor',
    'star_ratings',
    'bookstore',
    'blog',
    'django_feedparser',
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

ROOT_URLCONF = 'baitulilm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                # 'zinnia.context_processors.version',  # Optional
            ],
            # 'loaders': [
            #     'app_namespace.Loader',
            #     'django.template.loaders.filesystem.Loader',
            #     'django.template.loaders.app_directories.Loader',
            # ],
        },
    },
]

WSGI_APPLICATION = 'baitulilm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# cache settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/static/'

# defining a SITE_ID for django.contrib.sites
SITE_ID = 1

# STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# settings for static root and collecting static files
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# Uploaded Files ( Images, Text/PDF Files, Videos)
MEDIA_URL = '/media/'

# serving uploaded file in development
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = MEDIA_DIR

# email backend
# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
# EMAIL_BACKEND = "mailer.backend.DbBackend"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# MAILER_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # for mailer to know which email backend to use
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #printed in console

# Gmail email SMTP settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jattoade@gmail.com'
EMAIL_HOST_PASSWORD = 'jasabs93'

# Bookstore settings
# Django Star rating
# prevents re-rating an object
STAR_RATINGS_RERATE = False
# To enable anonymous rating
STAR_RATINGS_ANONYMOUS = True
STAR_RATINGS_STAR_HEIGHT = 32
STAR_RATINGS_STAR_WIDTH = 32


# django-tagging config
FORCE_LOWERCASE_TAGS = True
MAX_TAG_LENGTH = 20
# Django taggit settings
TAGGIT_CASE_INSENSITIVE = True

# django-zinnia-twitter Settings
# TWITTER_CONSUMER_KEY = ''
# TWITTER_CONSUMER_SECRET = ''
# TWITTER_ACCESS_KEY = ''
# TWITTER_ACCESS_SECRET = ''

# django-ckeditor settings for zinnia
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full' 'codeSnippets',
        'height': 400,
        'width': 1000,
        'extraPlugins': 'codesnippet',
    },
    # 'zinnia-content': {
    #     'toolbar_Zinnia': [
    #         ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
    #         ['Undo', 'Redo'],
    #         ['Scayt'],
    #         ['Link', 'Unlink', 'Anchor'],
    #         ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
    #         ['Source'],
    #         ['Maximize'],
    #         '/',
    #         ['Bold', 'Italic', 'Underline', 'Strike',
    #          'Subscript', 'Superscript', '-', 'RemoveFormat'],
    #         ['NumberedList', 'BulletedList', '-',
    #          'Outdent', 'Indent', '-', 'Blockquote'],
    #         ['Styles', 'Format'],
    #     ],
    #     'toolbar': 'Zinnia',
    # },
}

# setting for ckeditor upload file path
CKEDITOR_UPLOAD_PATH = "uploads/"
# other ckeditor settings
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_JQUERY_URL = '/static/js/jquery.min.js'
