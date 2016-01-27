# custom_storages.py
from django.conf import settings
from storages.backends.s3boto import S3BotoStorage
from filebrowser.storage import S3BotoStorageMixin

class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3BotoStorage, S3BotoStorageMixin):
    location = settings.MEDIAFILES_LOCATION
