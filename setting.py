STATIC_URL = '/static/'
STATIC_DIR =  os.path.join(BASE_DIR, 'static')

MEDIA_URL =  '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(BASE_DIR, '.static_root')