#!/usr/bin/env bash
export JUPYTER_CONFIG_DIR=$APP_HOME

jupyter notebook --no-browser --port 8080 --ip=0.0.0.0
