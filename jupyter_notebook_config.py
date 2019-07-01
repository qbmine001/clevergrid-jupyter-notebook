import os
from s3contents import S3ContentsManager

CELLAR_ADDON_KEY_ID = os.getenv("CELLAR_ADDON_KEY_ID")
CELLAR_ADDON_KEY_SECRET = os.getenv("CELLAR_ADDON_KEY_SECRET")
BUCKET_NOTEBOOK_NAME = os.getenv("BUCKET_NOTEBOOK_NAME")
CELLAR_ADDON_HOST = os.getenv("$CELLAR_ADDON_HOST")

c = get_config()

# Tell Jupyter to use S3ContentsManager for all storage.
c.NotebookApp.contents_manager_class = S3ContentsManager
c.S3ContentsManager.access_key_id = CELLAR_ADDON_KEY_ID
c.S3ContentsManager.secret_access_key = CELLAR_ADDON_KEY_SECRET
c.S3ContentsManager.bucket = BUCKET_NOTEBOOK_NAME
c.S3ContentsManager.endpoint_url = "https://" + CELLAR_ADDON_HOST

# Optional settings:
c.S3ContentsManager.prefix = ""
