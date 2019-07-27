from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_db',
        'USER': 'django',
        'PASSWORD': 'password123',
        'PORT': 5432,
        'HOST': 'localhost'
    }
}
