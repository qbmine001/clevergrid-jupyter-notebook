#!/usr/bin/env bash

mdkir $HOME/.jupyter

mv jupyter_notebook_config.py $HOME/.jupyter

jupyter notebook --no-browser --port 8080 --ip=0.0.0.0
