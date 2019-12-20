"""
Django settings for auction project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url

if os.path.exists('env.py'):
    import env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "sdfkjsdhfsdkjfhsdg"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", os.environ.get('AWS_C9_HOSTNAME'), os.environ.get('HEROKU_HOSTNAME')]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'accounts',
    'artifacts',
    'bidding',
    'mybiddings',
    'checkout',
    'search',
    'about',
    'storages'
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

ROOT_URLCONF = 'auction.urls'

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
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'auction.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


if "DATABASE_URL" in os.environ:
    print("This thing")
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

else:
    # So now Travis should be able to use the SQL database, as it does not have access to our cloud database.
    print("Database URL not found. Using SQLite instead")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

#aws s3 related
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000'
}

AWS_STORAGE_BUCKET_NAME = 'auctionmonica'
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_SECRET_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

#static
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth'
    
    # in the ecommerce video they used --> 'accounts.backends.CaseInsensitiveAuth'
    # in the auth miniproject the video used --> 'accounts.backends.EmailAuth'
]

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"