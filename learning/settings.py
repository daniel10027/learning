"""
Django settings for learning project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
import dj_database_url
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w%cuhsdmzmn1zux3xek@%aqx4_s9^zi4)x-@95j%8!mz3f4!+c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DEBUG_TOOLBAR_CONFIG = {
    # Toolbar options
    'RESULTS_CACHE_SIZE': 3,
    'SHOW_COLLAPSED': False,
    # Panel options
    'SQL_WARNING_THRESHOLD': 100,   # milliseconds
}


# Application definition

INSTALLED_APPS = [
    #################### ADMIN INTERFACE PACKAGES ################
    'admin_interface',
    'colorfield',
    ##############################################################
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 ]


INSTALLED_APPS += (
    
    'gestion',
    'enseignement',
    'recrutement',
    'configuration',
    'tinymce',
    'crispy_forms',
    'dynamic_formsets',
    'explorer',
    'debug_toolbar',
     'import_export',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
   
]

ROOT_URLCONF = 'learning.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
             os.path.join(BASE_DIR, 'templates')
             ],
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

WSGI_APPLICATION = 'learning.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


#Postgres
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'learning',

        'USER': 'daniel',

        'PASSWORD': '10027563kK#',

        'HOST': '127.0.0.1',

        'PORT': '5432',

    }

}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

##################################################
# SETTINGS +
##################################################
################# AUTHENTIFICATION ################
AUTH_USER_MODEL = 'gestion.User'
################# LOGIN AND LOGOUT ################
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'site-home'
LOGOUT_REDIRECT_URL = 'site-home'
################# MESSAGE #########################
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
################ CRISPY TEMPLATE PACK ############
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
BOOTSTRAP4 = {
    'include_jquery': True,
}
################ EMAIL CONFIGURATION #############
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'eduvroom@gmail.com'
EMAIL_HOST_PASSWORD = 'ccmutpghovhmqiaa'
EMAIL_PORT = 587
############### DEBUG TOOLBAR ####################
INTERNAL_IPS = [   
    '127.0.0.1', 
]
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]
############## GRAPH MODELS ######################
if DEBUG:
    INSTALLED_APPS += ['django_extensions']
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
############# EXPLORER SETTINGS ##################
EXPLORER_CONNECTIONS = {'Default':'default'}                
EXPLORER_DEFAULT_CONNECTION = 'default'
##################################################
X_FRAME_OPTIONS='SAMEORIGIN' 
##################################################

########  DATABASE OTHER CONFIGURATION ###########
#PhpMysql
"""
DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'name',
                'USER': 'user',
                'PASSWORD': 'password',
                'HOST': 'host',
                'PORT': 'port',
                'OPTIONS': {
                                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
                                }
                        }
            }
"""
#Sqlite
"""
DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }

"""
#ORACLE
django_heroku.settings(locals())