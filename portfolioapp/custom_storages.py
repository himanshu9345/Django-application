from django.conf import settings
from storages.backends.azure_storage import AzureStorage

class StaticStorage(AzureStorage):
    account_name = 'buildmyportfolio' # Must be replaced by your <storage_account_name>
    account_key = settings.AZURE_ACCOUNT_KEY # Must be replaced by your <storage_account_key>
    azure_container = 'sitedata/static'
    expiration_secs = None

class MediaStorage(AzureStorage):
    account_name = 'buildmyportfolio' # Must be replaced by your <storage_account_name>
    account_key = settings.AZURE_ACCOUNT_KEY# Must be replaced by your <storage_account_key>
    azure_container = 'sitedata/media'
    expiration_secs = None
