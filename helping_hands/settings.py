

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '*t^cd*-@@mqa36qnq*r&bz%j@($=*_33jxtlv_#0is1v$shwlk'

DEBUG = True

ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'helping_hands.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'helping_hands.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}




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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

# SENDGRID_API_KEY = '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'

# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
# SENDGRID_SANDBOX_MODE_IN_DEBUG=False

# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER= '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'
# EMAIL_HOST_PASSWORD= ' '


# Email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIT_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = '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'
# EMAIL_HOST_PASSWORD = 'SG.oDN9basdaECvH5asdasw.gXVEgtD1asqSkn-EW'


# SENDGRID_API_KEY = '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'

# EMAIL_BACKEND = "sgbackend.SendGridBackend"
# SENDGRID_SANDBOX_MODE_IN_DEBUG=False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'tsaicharan03@gmail.com'
EMAIL_HOST_PASSWORD = 'password'


