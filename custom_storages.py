from django.conf import settings
from storages.backends.azure_storage import AzureStorage

class StaticStorage(AzureStorage):
    account_name = 'buildmyportfolio' # Must be replaced by your <storage_account_name>
    account_key = 'pznNUsPouNWrFBoOHBVYidqDqwmrMfwAtddXhW86QLSADAGLwvl8tTVsoSaeFxo/s7GCgT8N+jFOCsXCRP894w==' # Must be replaced by your <storage_account_key>
    azure_container = 'sitedata/static'
    expiration_secs = None

class MediaStorage(AzureStorage):
    account_name = 'buildmyportfolio' # Must be replaced by your <storage_account_name>
    account_key = 'pznNUsPouNWrFBoOHBVYidqDqwmrMfwAtddXhW86QLSADAGLwvl8tTVsoSaeFxo/s7GCgT8N+jFOCsXCRP894w==' # Must be replaced by your <storage_account_key>
    azure_container = 'sitedata/media'
    expiration_secs = None
