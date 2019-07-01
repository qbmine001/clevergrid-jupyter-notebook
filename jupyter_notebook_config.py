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

from jupyters3 import JupyterS3, JupyterS3SecretAccessKeyAuthentication
c = get_config()
c.NotebookApp.contents_manager_class = JupyterS3

c.JupyterS3.aws_s3_bucket = "bucket-notebook"
c.JupyterS3.aws_s3_host = "cellar-c2.services.clever-cloud.com"
c.JupyterS3.prefix = ""

c.JupyterS3.authentication_class = JupyterS3SecretAccessKeyAuthentication

c.JupyterS3SecretAccessKeyAuthentication.aws_access_key_id = "89Y1283CC7J7Z596I92C"
c.JupyterS3SecretAccessKeyAuthentication.aws_secret_access_key = "8zTzWvbfJMCkhH9pgJo2gOmgxCwEu9N2LQwBhrUa"