#!/usr/bin/env bash

python ./bucket-management/bucket_management.py $CELLAR_ADDON_HOST $CELLAR_ADDON_KEY_ID $CELLAR_ADDON_KEY_SECRET --create-bucket $BUCKET_NOTEBOOK_NAME --ignore

jupyter notebook --no-browser --port 8080 --ip=0.0.0.0 --config=jupyter_notebook_config.py
