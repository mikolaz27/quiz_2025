from config.settings.base import *

SECRET_KEY = "django-insecure-mp3m1$h1($o)*wekb!t2=y$b^u)16t8gt)m6r$xbyxnx647l(4"

DEBUG = True

ALLOWED_HOSTS = []

# MIDDLEWARE + = ['']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "static/"