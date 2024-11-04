import os
from pathlib import Path
import environ
from django.contrib.messages import constants as messages

# Initialize the environment variables
env = environ.Env()

# Load the .env file
env_file = Path(__file__).resolve().parent.parent / '.env'
if env_file.exists():
    environ.Env.read_env(str(env_file))
    print(f".env file loaded from: {env_file}")
else:
    print(f".env file not found at: {env_file}")
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&!8-r8^t6(t!x@k)2yuvm(e^=_mn5v&g!x*ae4kllc8$ni5(m6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Myapp",
     'django_filters', #django filter is a library used for our filtering
    'phonenumber_field', 
    'django_countries', 
    'widget_tweaks',
    'crispy_forms',
    "crispy_bootstrap5",
    "verify_email.apps.VerifyEmailConfig",
   
    
]



CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Novaji1.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Novaji1.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Custom user model
AUTH_USER_MODEL = 'Myapp.User'
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


TML_MESSAGE_TEMPLATE = "welcome.txt"
REQUEST_NEW_EMAIL_TEMPLATE = 'custom.html'

LOGIN_URL = "login"
VERIFICATION_FAILED_TEMPLATE = "failed.html"

LOGIN_REDIRECT_URL = '/index/'
SUBJECT = 'Email Verification'
EXPIRE_AFTER = "5m" 
DEFAULT_FROM_EMAIL = 'noreply<Stitch.com>'

EMAIL_BACKEND = env('EMAIL_BACKEND')
RESEND_API_KEY = env('RESEND_API_KEY')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')