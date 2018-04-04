# Only set this to True in development environments
DEBUG = False
SHOW_BANNER = False
CAN_EDIT_ELECTIONS = False

# Set this to a long random string and keep it secret
# This is a handy tool:
# https://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = "{{ production_django_secret_key }}"
MEDIA_ROOT = "{{ django_media_root }}"
STATICFILES_DIRS = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{project_name}}',
        'USER': '{{postgres_username}}',
        'PASSWORD': '{{postgres_password}}',
        'HOST': '{{postgres_host}}',
    },
}

# A tuple of tuples containing (Full name, email address)
ADMINS = (
    ('YNR Prod Developers', 'developers+ynr-prod@democracyclub.org.uk')
)

SITE_WIDE_MESSAGES = [
    {
        'message': """
            Election data parties! Join us on the 10th of April in London,
            Birmingham or Manchester for one of our famous SOPN parties!
        """,
        'show_until': "2018-04-10T18:00",
        'url': "https://democracyclub.org.uk/blog/2018/03/29/election-data-parties/"
    }
]



# **** Other settings that might be useful to change locally

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1', 'localhost', ]

CACHES = {
    'default': {
        'TIMEOUT': None,  # cache keys never expire; we invalidate them
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': DATABASES['default']['NAME'],
    },
    'thumbnails': {
        'TIMEOUT': 60 * 60 * 24 * 2,  # expire after two days
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': DATABASES['default']['NAME'] + "-thumbnails",
    },
}


# **** Settings that might be useful in production

TWITTER_APP_ONLY_BEARER_TOKEN = "{{TWITTER_APP_ONLY_BEARER_TOKEN}}"
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
RAVEN_CONFIG = {
    'dsn': '{{RAVEN_DSN}}'
}

RUNNING_TESTS = False
