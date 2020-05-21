import os

__STATIC_PATH = os.path.dirname(os.path.dirname(__file__))

DEFAULT_FILE_STORAGE = (
    'tenant_schemas.storage.TenantFileSystemStorage'
)

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(__STATIC_PATH, "../djflow/static"),
    os.path.join(__STATIC_PATH, "../djflow/apps/security/static"),
)

STATIC_ROOT = os.path.join(__STATIC_PATH, '../static/')
