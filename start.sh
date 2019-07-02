#!/usr/bin/env bash

# Create a storage bucket if it not exists
python ./bucket-management/bucket_management.py $CELLAR_ADDON_HOST $CELLAR_ADDON_KEY_ID $CELLAR_ADDON_KEY_SECRET --create-bucket $BUCKET_NOTEBOOK_NAME --ignore

# Run jupyter on the port 8080, granted remote access and set a specific jupyter configuration file
jupyter notebook --no-browser --port 8080 --ip=0.0.0.0 --config=jupyter_notebook_config.py
