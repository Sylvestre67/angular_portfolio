"""
Django settings for sg_portfolio project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR_HEROKU = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS = os.path.join(BASE_DIR,'templates')
STATIC_DIRS = os.path.join(BASE_DIR,'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/



# Allow all host headers
ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'storages',
    'django_seo_js',
    'pfolio',
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django_seo_js.middleware.EscapedFragmentMiddleware',  # If you're using #!
    'django_seo_js.middleware.UserAgentMiddleware',  # If you want to detect by user agent
)

ROOT_URLCONF = 'sg_portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIRS],
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

WSGI_APPLICATION = 'sg_portfolio.wsgi.application'

# Email
# PostmarkApp
if os.getenv('POSTMARK_API_TOKEN'):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.postmarkapp.com'
    EMAIL_HOST_PASSWORD = os.environ['POSTMARK_API_TOKEN']
    EMAIL_HOST_USER = os.environ['POSTMARK_API_TOKEN']
    EMAIL_PORT = '587'
    EMAIL_USE_TLS = True
    SERVER_EMAIL = os.environ['POSTMARK_INBOUND_ADDRESS']
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
if os.getenv('DATABASE_URL'):
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('RDS_DB_NAME'),
            'USER': os.getenv('RDS_USERNAME'),
            'PASSWORD': os.getenv('RDS_PASSWORD'),
            'HOST': os.getenv('RDS_HOSTNAME'),
            'PORT': os.getenv('RDS_PORT'),
        }
    }

    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()
    DATABASES['default']['CONN_MAX_AGE'] = 500

    #AWS SETTINGS
    AWS_STORAGE_BUCKET_NAME = 'sg-pfolio'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    # Tell django-storages that when coming up with the URL for an item in S3 storage, keep
    # it simple - just use this domain plus the path. (If this isn't set, things get complicated).
    # This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
    # We also use it in the next setting.
    STATICFILES_LOCATION = 'static'
    #STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    #STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
    #ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'

    # Media files on S3 configuration
    MEDIA_ROOT = 'media'
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

    #DJANGO-SEO-JS
    SEO_JS_PRERENDER_TOKEN = os.environ['PRERENDER_TOKEN']

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'sg-pfolio'
            #'USER': 'postgres',
            #'PASSWORD': 'noosfere',
            #'HOST': '127.0.0.1',
            #'PORT': '5432',
        }
    }


    # Uploaded Media files
    MEDIA_URL = '/media/'
    MEDIA_ROOT = 'media'

    INTERNAL_IPS = ['127.0.0.1','0.0.0.0']

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '111'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    #DJANGO-SEO-JS
    SEO_JS_PRERENDER_TOKEN='123456789abjdefgj'

#Static files (CSS, JavaScript, Images)
#https://docs.djangoproject.com/en/1.8/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    STATIC_DIRS,
    os.path.join(BASE_DIR_HEROKU, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



TEMPLATE_DIRS = [
    #TEMPLATE_DIRS,
    os.path.join(BASE_DIR,  'templates'),
]


