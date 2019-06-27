import os
from jupters3 import JupyterS3, JupyterS3SecretAccessKeyAuthentication

CELLAR_ADDON_HOST = os.getenv("CELLAR_ADDON_HOST")
CELLAR_ADDON_KEY_ID = os.getenv("CELLAR_ADDON_KEY_ID")
CELLAR_ADDON_KEY_SECRET = os.getenv("CELLAR_ADDON_KEY_SECRET")

CELLAR_BUCKET_NAME = "test_jupyter"

c = get_config()
c.NotebookApp.contents_manager_class = JupyterS3
c.JupyterS3.aws_s3_host = CELLAR_ADDON_HOST
c.JupyterS3.aws_s3_bucket = CELLAR_BUCKET_NAME
c.JupyterS3.authentication_class = JupyterS3SecretAccessKeyAuthentication

c.JupyterS3SecretAccessKeyAuthentication.aws_access_key_id	= CELLAR_ADDON_KEY_ID
c.JupyterS3SecretAccessKeyAuthentication.aws_secret_access_key = CELLAR_ADDON_KEY_SECRET