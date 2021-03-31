DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_appdb',
        'USER': 'django_app',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

#################################################################
    ##  (CORS) Cross-Origin Resource Sharing Settings ##
#################################################################
CORS_ORIGIN_ALLOW_ALL = True