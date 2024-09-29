"""
Django settings for api_core project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/


from api_core import (
    BASE_DIR,
    #* Load the .env file
    SECRET_KEY, # SECURITY WARNING: keep the secret key used in production secret!
    DEBUG, # SECURITY WARNING: don't run with debug turned on in production!
)



# SECURITY WARNING: keep the secret key used in production secret!

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', #* Turn off the admin when using Restfull API
    'django.contrib.auth',
    'django.contrib.contenttypes', #* Turn off the contenttypes when using Restfull API
    'django.contrib.sessions', #* Turn off the contenttypes when using Restfull API
    'django.contrib.messages', #* Turn off the contenttypes when using Restfull API
    'django.contrib.staticfiles', #* Turn off the contenttypes when using Restfull API
    #* Libraries Apps
    'corsheaders',
    'ninja_extra',
    'ninja_jwt',
    # 'django_extensions' if DEBUG else '',
    #* My Apps
    'app_v1',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api_core.api'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'api_core.deployment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# postgresql://postgres.bohxofxwmrvpxttxpblr:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres

LIST_DATABASE = [
    {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.bohxofxwmrvpxttxpblr',
        'PASSWORD': '@S2001phamhai',
        'HOST': 'aws-0-ap-southeast-1.pooler.supabase.com',
        'PORT': '6543',
    },
    {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djex-next',
        'USER': 'postgres',
        'PASSWORD': 'anhtudev2003',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
]

DATABASES = {
    'default': LIST_DATABASE[0]
}
DEFAULT_CHARSET = 'utf-8'


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'vi-vn'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#* Custom User Model
AUTH_USER_MODEL = 'app_v1.User'

#* Ninja Extra Pagination
NINJA_EXTRA={
    'PAGINATION_CLASS': 'api_core.dev.pagination.custom.CustomPagination',
}

#* Custom Devs
from .dev import (
    #* Custom JWT
    NINJA_JWT, 
    #* Cors Headers
    CORS_ALLOWED_ORIGINS, 
    CORS_ALLOW_CREDENTIALS,
    CORS_ALLOW_METHODS,
    CORS_ALLOW_HEADERS,
    CORS_ALLOW_ALL_ORIGINS,
    CORS_ALLOW_PRIVATE_NETWORK,
)


