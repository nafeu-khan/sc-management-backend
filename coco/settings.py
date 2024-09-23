import os
from decouple import config
from django.utils.translation import gettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-3w)n^2u6--w92toyn6@1yc=2ka!l+22_hujwmq3s#yynk1+-is"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "simple_history",
    "corsheaders",
    "debug_toolbar",
    "drf_yasg",
    "csp",
    "security",
    "contact_app",
    "defender",
    "common",  # As the foundational app
    "educational_organizations_app",  # Depends on `common`
    "auth_app",  # Assuming it doesn't depend on the specific structure of the earlier apps
    "profile_app",  # Assuming it's independent or only lightly dependent on the earlier apps
    "university_app",  # Assuming it's independent or depends on earlier listed apps
    "log_viewer",
    "campus_app",
    "college_app",
    "department_app",
    "faculty_members_app",
    "rosetta",
    "phonenumber_field",
    "user_app"
]
PHONENUMBER_DEFAULT_REGION = 'US' 

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'scs.middleware.RateLimitMiddleware',
    "csp.middleware.CSPMiddleware",
    'defender.middleware.FailedLoginMiddleware',
]

ROOT_URLCONF = "scs.urls"

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]

CORS_ALLOW_CREDENTIALS = True

INTERNAL_IPS = [
    '127.0.0.1'
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'emails')],
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

WSGI_APPLICATION = "scs.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

LANGUAGES = [
    ('en', _('English')),
    ('bn', _('Bengali')),
    ('fr', _('French'))
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

USE_I18N = True
USE_L10N = True


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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': "Token-based authentication with required prefix 'Token'",
        }
    },
    'USE_SESSION_AUTH': False,
    'DEFAULT_API_KEY': 'Token 89b507c6b45cf9067d9765a4edec61bfc433bf0f',  # Default token for testing
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
LOGS_ROOT=os.path.join(BASE_DIR, 'logs')


# settings.py

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = (
    "'self'", "'unsafe-inline'", "'unsafe-eval'", "http://localhost:3000", 
    "https://www.google.com", "https://www.gstatic.com", "https://www.recaptcha.net"
)
CSP_STYLE_SRC = (
    "'self'", "'unsafe-inline'", "http://localhost:3000", 
    "https://fonts.googleapis.com"
)
CSP_IMG_SRC = (
    "'self'", "data:", "http://localhost:3000", 
    "https://www.google.com", "https://www.gstatic.com"
)
CSP_FONT_SRC = ("'self'", "http://localhost:3000", "https://fonts.gstatic.com")
CSP_CONNECT_SRC = ("'self'", 'https://api.example.com')  # Allow AJAX, WebSocket connections from the same origin and specific domains
CSP_FRAME_SRC = (
    "'self'", "https://www.google.com/", "https://www.recaptcha.net/", 
    "https://another-allowed-source.com/", "https://yet-another-source.com/"
)
CSP_BASE_URI = ("'self'",)
CSP_FORM_ACTION = ("'self'",)
CSP_REPORT_URI = '/csp-report/'
DEFENDER_REDIS_URL = os.getenv('DEFENDER_REDIS_URL', 'redis://localhost:6379/0')
DEFENDER_LOGIN_FAILURE_LIMIT= int(os.getenv('DEFENDER_LOGIN_FAILURE_LIMIT'))
DEFENDER_COOLOFF_TIME=int(os.getenv('DEFENDER_COOLOFF_TIME'))
DEFENDER_LOCKOUT_COOLOFF_TIME=int(os.getenv('DEFENDER_LOCKOUT_COOLOFF_TIME'))
DEFENDER_GET_USERNAME_FROM_REQUEST_PATH = 'auth_app.utils.custom_username_from_request'
DEFENDER_LOCKOUT_URL = 'lockout'
# DEFENDER_DISABLE_IP_LOCKOUT=True
# DEFENDER_LOGIN_FAILURE_LIMIT_USERNAME=   #
# DEFENDER_LOGIN_FAILURE_LIMIT_IP=       #
# DEFENDER_LOCKOUT_URL=   #redirect link
# DEFENDER_LOCK_OUT_BY_IP_AND_USERNAME=  #



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/info.log',
            'formatter': 'verbose',
        },
        'file_warning': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/warning.log',
            'formatter': 'verbose',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/error.log',
            'formatter': 'verbose',
        },
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/debug.log',
            'formatter': 'verbose',
        },
        'file_critical': {
            'level': 'CRITICAL',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/critical.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file_info', 'file_warning', 'file_error', 'file_debug', 'file_critical'],
            'level': 'DEBUG',  # Set the root logger level to the lowest level you want to capture
            'propagate': True,
        },
    },
}




LOG_VIEWER_FILES = ['info.log', 'warning.log', 'error.log', 'debug.log', 'critical.log']
LOG_VIEWER_FILES_PATTERN = '*.log*'
LOG_VIEWER_FILES_DIR = BASE_DIR / 'logs/'
LOG_VIEWER_PAGE_LENGTH = 25       # Total log lines per page
LOG_VIEWER_MAX_READ_LINES = 1000  # Total log lines to read
LOG_VIEWER_FILE_LIST_MAX_ITEMS_PER_PAGE = 25  # Max log files loaded in Datatable per page
LOG_VIEWER_PATTERNS = ['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL']
LOG_VIEWER_EXCLUDE_TEXT_PATTERN = None  # String regex expression to exclude log lines
