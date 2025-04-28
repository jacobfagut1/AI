# settings.py

# Secret Key, Debug, and Allowed Hosts
SECRET_KEY = 'django-insecure-$sn*ilosstwg2ad=ew#^+lnjpu&@et4#h6k=bblc$h^vws@%r2'  # Replace with your actual secret key
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = ['ai-5k1u.onrender.com', 'localhost', '127.0.0.1']

# OpenAI Key (API Key)
OPENAI_KEY = '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'


# settings.py
GEMINI_API_KEY = 'AIzaSyA2FCqEkieRKAYxObBmb-quPb_TBEQU8x0'  # Replace with your actual Gemini API key
# MongoDB URI
MONGO_URI = 'mongodb+srv://mjefagut01:secretpassword@cluster0.9lahgmr.mongodb.net/ecommerce_db?retryWrites=true&w=majority'  # Replace with your actual MongoDB URI

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'djongo',
    'taggit',
    'openai',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


WSGI_APPLICATION = 'ecommerce_project.wsgi.application'

# Database configuration for MongoDB using Djongo
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'ecommerce_db',  # The name of your MongoDB database
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': MONGO_URI,  # MongoDB URI defined earlier
        },
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'