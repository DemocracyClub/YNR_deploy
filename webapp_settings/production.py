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

HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
        'URL': '{{ AWS_EX_URL }}',
        'INDEX_NAME': 'ynr_prod',
    },
}

CELERY_BROKER_URL = "redis://localhost:6379/0"

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


# This should be one of:
# ELECTION_STATS
# SOPN_TRACKER
# RESULTS_PROGRESS
# BY_ELECTIONS
FRONT_PAGE_CTA = 'BY_ELECTIONS'
SOPN_TRACKER_INFO = {
    # Will be used as "{} nomination papers (SOPNs)"
    # and "Help us find all the nomination papers for the {}s"
    # Note the trailing 's' is added in the latter case
    'election_name': "Local elections in England",
    'election_date': '2018-05-03',
}

SCHEDULED_ELECTION_DATES = [
    "2019-05-02"
]


STATICFILES_STORAGE = 'ynr.s3_storage.StaticStorage'
DEFAULT_FILE_STORAGE= 'ynr.s3_storage.MediaStorage'
AWS_S3_REGION_NAME = 'eu-west-2'
AWS_STORAGE_BUCKET_NAME = "static-candidates.democracyclub.org.uk"
AWS_S3_CUSTOM_DOMAIN = "static-candidates.democracyclub.org.uk"
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

CSRF_TRUSTED_ORIGINS = [
    "{{ domain }}",
]

USE_X_FORWARDED_HOST = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_HOST = 'email-smtp.eu-west-1.amazonaws.com'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '{{smtp_username}}'
EMAIL_HOST_PASSWORD = '{{smtp_password}}'


#  Send errors to sentry by default
LOGGING['handlers']['sentry'] = {
    'level': 'WARNING',
    'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
}
LOGGING["loggers"]["account_adapter"]: {
    'level': 'WARNING',
    'handlers': ['sentry'],
    'propagate': False,
}


SLACK_TOKEN = "{{slack_token}}"
