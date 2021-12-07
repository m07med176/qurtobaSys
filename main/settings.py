"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '-8s9ut4mjnvn3muph+%7cab8%7&ilw%bb&5w%mndt0rkp+7+k-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['qurtoba.herokuapp.com','127.0.0.1','192.168.1.109']


INSTALLED_APPS = [
    # Third Party #
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Utils #
    'phone_field',
    'crispy_forms',
    'search_admin_autocomplete',
    'rest_framework',
    'rest_framework.authtoken',
    'debug_toolbar',
    'django_filters',
    # Apps #
    'account',
    'homeApp',
    'customers',
    'dataEltogarApp',
    'transactions',
    'fawryCodesApp',
    'vonoApp',

    'storeApp',
    'productsSelesApp',
    'fawrySelesApp',
    'sellersApp',
    'shakawaApp',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'customers.utils.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':100,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        ),
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',
    ),
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ 'templates'],
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



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd84lv9hqj4cvad',
        'HOST': 'ec2-34-254-69-72.eu-west-1.compute.amazonaws.com',
        'PORT': 5432,
        'USER': 'pkekjaplofajah',
        'PASSWORD': '5f23b729fd13ec1e966727ead1da9717e48c44bd830a6753ee23f54e14d3b099',
    }
}

WSGI_APPLICATION = 'main.wsgi.application'
AUTH_USER_MODEL = 'account.Account' 
AUTHENTICATION_BACKENDS = ( 
    'django.contrib.auth.backends.AllowAllUsersModelBackend', 
    'account.backends.CaseInsensitiveModelBackend',
    )
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760 # 10mb = 10 * 1024 *1024
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Africa/Cairo'
DATETIME_FORMAT = '%Y-%m-%d %H:%m'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

INTERNAL_IPS = [
    '127.0.0.1',
]
