#!/usr/bin/env bash

jupyter serverextension enable --py bookstore
jupyter notebook --no-browser --port 8080 --ip=0.0.0.0 --config=jupyter_notebook_config.py --notebook-dir=$APP_HOME/workdir
