# from bookstore import BookstoreContentsArchiver
#
#
# c.NotebookApp.contents_manager_class = BookstoreContentsArchiver
#
# c.BookstoreSettings.workspace_prefix = "/workspace/notebooks"
# c.BookstoreSettings.published_prefix = "/published/notebooks"
#
# c.BookstoreSettings.s3_bucket = "bucket-notebook"
#
# c.BookstoreSettings.s3_access_key_id = "89Y1283CC7J7Z596I92C"
# c.BookstoreSettings.s3_secret_access_key = "8zTzWvbfJMCkhH9pgJo2gOmgxCwEu9N2LQwBhrUa"
# c.BookstoreSettings.s3_endpoint_url = "cellar-c2.services.clever-cloud.com"

# from jupyters3 import JupyterS3, JupyterS3SecretAccessKeyAuthentication
# c = get_config()
# c.NotebookApp.contents_manager_class = JupyterS3
#
# c.JupyterS3.aws_s3_bucket = "bucket-notebook"
# c.JupyterS3.aws_s3_host = "cellar-c2.services.clever-cloud.com"
# c.JupyterS3.prefix = ""
#
# c.JupyterS3.authentication_class = JupyterS3SecretAccessKeyAuthentication
#
# c.JupyterS3SecretAccessKeyAuthentication.aws_access_key_id = "89Y1283CC7J7Z596I92C"
# c.JupyterS3SecretAccessKeyAuthentication.aws_secret_access_key = "8zTzWvbfJMCkhH9pgJo2gOmgxCwEu9N2LQwBhrUa"

from s3contents import S3ContentsManager

c = get_config()

# Tell Jupyter to use S3ContentsManager for all storage.
c.NotebookApp.contents_manager_class = S3ContentsManager
c.S3ContentsManager.access_key_id = "89Y1283CC7J7Z596I92C"
c.S3ContentsManager.secret_access_key = "8zTzWvbfJMCkhH9pgJo2gOmgxCwEu9N2LQwBhrUa"
c.S3ContentsManager.bucket = "bucket-notebook"
.S3ContentsManager.endpoint_url = "cellar-c2.services.clever-cloud.com"

# Optional settings:
c.S3ContentsManager.prefix = ""
