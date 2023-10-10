# dierenhulp/settings.py

from dotenv import load_dotenv

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv( BASE_DIR / '.env', )

# settings for Windows 10 with GDAL
if os.name == 'nt':
  VENV_BASE = os.environ['VIRTUAL_ENV']
  os.environ['PATH']     = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo') + ';' + os.environ['PATH']
  os.environ['PROJ_LIB'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo\\data\\proj') + ';' + os.environ['PATH']

SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  #'django.contrib.gis',
  # apps
  'users.apps.UsersConfig',
  'nestkasten.apps.NestkastenConfig',
  'chargestations.apps.ChargestationsConfig',
  'mushrooms.apps.MushroomsConfig',
  # support packages
  'django_extensions', # django-extentions
  'leaflet', # django-leaflet
  'djgeojson', # django-geojson
  'gisserver', # django-gisserver
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

ROOT_URLCONF = 'dierenhulp.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'dierenhulp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    #'ENGINE': 'django.contrib.gis.db.backends.spatialite',
    'NAME'  : BASE_DIR / 'db.sqlite3',
  }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'Europe/Amsterdam'
USE_I18N      = True
USE_TZ        = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_DIRS = [
  BASE_DIR / 'static',
  BASE_DIR / 'media',
]    # Django zoekt altijd in de static-folder van de app, maar daarnaast ook op deze lokatie(s)

STATIC_URL  = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL   = '/media/'                # URL via welke mediafiles toegankelijk zijn van buiten de app
MEDIA_ROOT  = BASE_DIR / 'mediafiles'  # absoluut pad waar project mediafiles worden opgeslagen

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django-leaflet configuratie
LEAFLET_CONFIG = {
  'DEFAULT_CENTER'     : (52.5, 4.95),
  'DEFAULT_ZOOM'       : 12,
  'MIN_ZOOM'           : 3,
  'MAX_ZOOM'           : 18,
  'DEFAULT_PRECISION'  : 6,
  'ATTRIBUTION_PREFIX' : 'Powered by datalab',
  'SCALE'              : 'metric',
  'RESET_VIEW'         : False,
  #'MINIMAP'            : True,
  'PLUGINS': {
    'draw': {
      'css': ['https://cdnjs.cloudflare.com/ajax/libs/leaflet.draw/1.0.4/leaflet.draw.css',],
      'js': 'https://cdnjs.cloudflare.com/ajax/libs/leaflet.draw/1.0.4/leaflet.draw.js',
      'auto-include': True,
    },
  },
}