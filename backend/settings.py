import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------
# Security
# ------------------------------
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-654sqqmj9yt4qb@$m(7+!$*r!fuk+yz-#3zr2s#6c3$qb)e9#q"
)

DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

# ALLOWED_HOSTS: default to localhost for dev, Render URL for production
ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS",
    "localhost 127.0.0.1 fs-django-backend-2.onrender.com"
).split()

# ------------------------------
# Apps
# ------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "corsheaders",
    "rest_framework",

    # Local apps
    "base",
]

# ------------------------------
# Middleware
# ------------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # Must be at top
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

# ------------------------------
# Database
# ------------------------------
# Local default is Railway; override with Render env vars in production
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PGNAME", "railway"),
        "USER": os.environ.get("PGUSER", "postgres"),
        "PASSWORD": os.environ.get(
            "PGPASSWORD", "hVzZeJlXMoUECQJzEtILlnLoJgVryDNx"
        ),
        "HOST": os.environ.get("PGHOST", "shuttle.proxy.rlwy.net"),
        "PORT": os.environ.get("PGPORT", "18727"),
    }
}

# ------------------------------
# Password Validators
# ------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ------------------------------
# Internationalization
# ------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------
# Static & Media
# ------------------------------
STATIC_URL = 'static/'
MEDIA_URL = '/images/'
MEDIA_ROOT = BASE_DIR / 'static/images'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------------------------
# CORS
# ------------------------------
CORS_ALLOWED_ORIGINS = os.environ.get(
    "CORS_ALLOWED_ORIGINS",
    "http://localhost:5173 http://127.0.0.1:5173 http://localhost:5174 http://127.0.0.1:5174 https://demitime.netlify.app"
).split()
