# Minimal settings file

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'with_asserts.sqlite',
    }
}

DEBUG = True
TEMPLATE_DEBUG = DEBUG
INSTALLED_APPS = (
    'simple',
)

ROOT_URLCONF = 'project.urls'

SECRET_KEY = '=#t$o1in0&q(-bewo=4==$!wj7!i0$s%9%b#x*n@i_ak%khg*k'
