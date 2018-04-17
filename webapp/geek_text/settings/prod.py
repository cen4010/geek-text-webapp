from .base import *
import dj_database_url

ENVIRONMENT = 'prod'
DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com', '*', 'geek-text.herokuapp.com']
SECRET_KEY = os.environ.get('SECRET_KEY', 'MISSING SECRET_KEY')

#print(os.environ.get('DATABASE_URL', 'foooo DATABASE_URL'))

# CI Hooks
USER = os.environ.get('USER', os.environ.get('USERNAME', 'ANON-DEV'))
CI_ENV = 'dev/' + USER
if os.environ.get('CI', 'false') == 'true':
    CI_ENV = 'ci/' + os.environ.get('CI_COMMIT', 'HASHLESS')
    if os.environ.get('TRAVIS_BRANCH', 'nil') == 'master':
        CI_ENV = 'geek-text'

# Database
DATABASES['default'] = dj_database_url.config(
            default=os.environ.get('DATABASE_URL', 'MISSING DATABASE_URL'))

# Storage
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static/%s' % CI_ENV
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media/%s' % CI_ENV

# AWS Auth
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_ID', 'MISSING AWS ACCESS ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY', 'MISSING AWS SECRET KEY')

# AWS S3 Config
AWS_S3_REGION_NAME = 'us-east-1'
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET', 'MISSING AWS S3 BUCKET')
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
## AWS Bucket URL
AWS_S3_CUSTOM_DOMAIN = 's3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME
