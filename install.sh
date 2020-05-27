#!/bin/bash

python3 setup.py sdist bdist_wheel
pip uninstall dist/healthcheck_malay-0.0.1-py3-none-any.whl
pip install dist/healthcheck_malay-0.0.1-py3-none-any.whl