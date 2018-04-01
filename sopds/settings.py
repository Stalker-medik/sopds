"""
Django settings for sopds project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys
from collections import OrderedDict

from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm4l1c#nq6*zs!c3ri4dg4(54_7bvrl5uintni6p20tijlaxv!x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',    
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',    
    'opds_catalog',
    'sopds_web_backend',    
    'django.contrib.admin',   
    'django.contrib.staticfiles',     
    'constance.backends.database',
    'constance',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',    
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'opds_catalog.middleware.SOPDSLocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.cache.CacheMiddleware',
    #'opds_catalog.middleware.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'sopds.urls'

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
                'django.contrib.messages.context_processors.messages',
                'sopds_web_backend.views.sopds_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'sopds.wsgi.application'

#### SOPDS DATABASE SETTINGS START ####

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

#DATABASES = {    
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'sopds',
#        'HOST': 'localhost',
#        'USER': 'sopds',
#        'PASSWORD' : 'sopds',
#        'OPTIONS' : {
#            'init_command': "SET default_storage_engine=MyISAM;\
#                             SET sql_mode='';"
#        }
#    }             
#}

#DATABASES = {
#    'default': {
#    'ENGINE': 'django.db.backends.postgresql_psycopg2',
#    'NAME': 'sopds',
#    'USER': 'sopds',
#    'PASSWORD': 'sopds',
#    'HOST': '', # Set to empty string for localhost.
#    'PORT': '', # Set to empty string for default.
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }         
}

#### SOPDS DATABASE SETTINGS FINISH ####

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/1.9/topics/i18n/
    
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'sopds/locale'),
)

TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

CACHE_BACKEND = "locmem://"
CACHE_MIDDLEWARE_KEY_PREFIX = "sopds"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = 'static'

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_ADDITIONAL_FIELDS = {
    'language_select': ['django.forms.fields.ChoiceField', {
        'widget': 'django.forms.Select',
        'choices': (("ru-RU", "Russian"), ("en-US", "English"))
    }],
}

CONSTANCE_CONFIG = OrderedDict([
    ('SOPDS_LANGUAGE', ('en-US',_('Select language'),'language_select')),    
    ('SOPDS_ROOT_LIB', ('books/',_('Absolute path to books collection directory'))),
    ('SOPDS_BOOK_EXTENSIONS', ('.pdf .djvu .fb2 .epub .mobi', _('List of managed book files extensions'))),
    ('SOPDS_SCAN_START_DIRECTLY', (False,_('Turn once scanning directly'))),
    ('SOPDS_CACHE_TIME', (1200, _('Pages cache time'))),

    ('SOPDS_TELEBOT_API_TOKEN', ('', _('Telegramm API Token'))),
    ('SOPDS_TELEBOT_AUTH', (True,_('Enable telebot authentication. Test presense telegram username in local users database (case insensetive).'))),
    ('SOPDS_TELEBOT_MAXITEMS', (10, _('Max items on page'))),
    
    ('SOPDS_AUTH', (True,_('Enable authentication'))),
    ('SOPDS_ALPHABET_MENU', (True,_('Enable alphabet submenu'))),   
    ('SOPDS_DOUBLES_HIDE', (True,_('This flag hides found doublicates'))),
    ('SOPDS_COVER_SHOW', (True,_('This flag activate showing cover of books'))),
    ('SOPDS_SPLITITEMS', (300,_('Max subitems count in alphabet menuitem'))),
    ('SOPDS_MAXITEMS', (60,_('Max items on page'))),
    ('SOPDS_TITLE_AS_FILENAME', (True,_('Create downloaded filename from book title'))),
    ('SOPDS_NOCOVER_PATH', (os.path.join(BASE_DIR,'static/images/nocover.jpg'),_('Path to image file showing for book without embedded cover'))),    
        
    
    ('SOPDS_FB2SAX', (True,_('This flag activate SAX Parser for FB2 instead of lxml.xpath'))),
    ('SOPDS_ZIPSCAN', (True,_('This flag activate zip files scanning'))),
    ('SOPDS_ZIPCODEPAGE', ('cp866',_('Set codepage for filenames inside zipfile'))),
    ('SOPDS_INPX_ENABLE', (False,_('Enables read metadata from inpx-file (and stop scanning deeper from ipx-file place)'))),
    ('SOPDS_INPX_SKIP_UNCHANGED', (True,_('Skip scanning INPX with unchanged size after previous scan'))),
    ('SOPDS_INPX_TEST_ZIP', (False,_('Test avialability zip files listed in INPX before add in collection'))),
    ('SOPDS_INPX_TEST_FILES', (False,_('Test avialability book files listed in INPX before add in collection'))),
    ('SOPDS_DELETE_LOGICAL', (False,_('Logical deleting unavialable files'))),
    
    ('SOPDS_SCAN_SHED_MIN', ('0',_('sheduled minutes for sopds_scanner (cron syntax)'))),
    ('SOPDS_SCAN_SHED_HOUR', ('0,12',_('sheduled hours for sopds_scanner (cron syntax)'))),
    ('SOPDS_SCAN_SHED_DAY', ('*',_('sheduled day for sopds_scanner (cron syntax)'))),
    ('SOPDS_SCAN_SHED_DOW', ('*',_('sheduled day of weeks for sopds_scanner (cron syntax)'))),  
    
    ('SOPDS_FB2TOEPUB', ('',_('Path to FB2-EPUB converter program'))),
    ('SOPDS_FB2TOMOBI', ('',_('Path to FB2-MOBI converter program'))),
    ('SOPDS_TEMP_DIR', (os.path.join(BASE_DIR,'tmp'),_('Path to temporary files directory'))),

    ('SOPDS_SERVER_LOG', (os.path.join(BASE_DIR,'opds_catalog/log/sopds_server.log'),_('Path to logfile for sopds_server process'))),
    ('SOPDS_SCANNER_LOG', (os.path.join(BASE_DIR,'opds_catalog/log/sopds_scanner.log'),_('Path to logfile for sopds_scanner process'))),
    ('SOPDS_TELEBOT_LOG', (os.path.join(BASE_DIR, 'opds_catalog/log/sopds_telebot.log'), _('Path to logfile for sopds_telebot process'))),
    ('SOPDS_SERVER_PID', (os.path.join(BASE_DIR,'opds_catalog/tmp/sopds_server.pid'),_('Path to pidfile for sopds_server process'))),
    ('SOPDS_SCANNER_PID', (os.path.join(BASE_DIR,'opds_catalog/tmp/sopds_scanner.pid'),_('Path to pidfile for sopds_scanner process'))),
    ('SOPDS_TELEBOT_PID', (os.path.join(BASE_DIR, 'opds_catalog/tmp/sopds_telebot.pid'), _('Path to pidfile for sopds_telebot process'))),
                      
])

CONSTANCE_CONFIG_FIELDSETS = {
    '1. General Options': ('SOPDS_LANGUAGE', 'SOPDS_ROOT_LIB', 'SOPDS_BOOK_EXTENSIONS','SOPDS_CACHE_TIME', 'SOPDS_SCAN_START_DIRECTLY'),
    '2. Server Options': ('SOPDS_AUTH', 'SOPDS_ALPHABET_MENU', 'SOPDS_DOUBLES_HIDE', 'SOPDS_COVER_SHOW', 'SOPDS_SPLITITEMS', 'SOPDS_MAXITEMS', 'SOPDS_TITLE_AS_FILENAME', 'SOPDS_NOCOVER_PATH'),    
    '3. Scanner Options': ('SOPDS_FB2SAX','SOPDS_ZIPSCAN','SOPDS_ZIPCODEPAGE', 'SOPDS_INPX_ENABLE', 'SOPDS_INPX_SKIP_UNCHANGED', 'SOPDS_INPX_TEST_ZIP', 'SOPDS_INPX_TEST_FILES', 'SOPDS_DELETE_LOGICAL'),
    '4. Scanner Shedule': ('SOPDS_SCAN_SHED_MIN', 'SOPDS_SCAN_SHED_HOUR', 'SOPDS_SCAN_SHED_DAY','SOPDS_SCAN_SHED_DOW'),
    '5. Telegramm Bot Options': ('SOPDS_TELEBOT_API_TOKEN','SOPDS_TELEBOT_AUTH','SOPDS_TELEBOT_MAXITEMS'),
    '6. Converters Options': ('SOPDS_FB2TOEPUB', 'SOPDS_FB2TOMOBI', 'SOPDS_TEMP_DIR'),
    '7. Log & PID Files': ('SOPDS_SERVER_LOG', 'SOPDS_SCANNER_LOG', 'SOPDS_TELEBOT_LOG','SOPDS_SERVER_PID','SOPDS_SCANNER_PID','SOPDS_TELEBOT_PID'),
}


