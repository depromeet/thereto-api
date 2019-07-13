DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTH_APPS = [
    'rest_framework',
    'corsheaders',
    'drf_yasg',
]

PROJECT_APPS = [
    'apps.friend',
    'apps.letter',
    'apps.user',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTH_APPS + PROJECT_APPS
