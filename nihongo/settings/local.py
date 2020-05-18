from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$98@1hoo@6ndu=$5q1il6p6ixp)$qo_^=asdqj(vvjackq4!q^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}