#!/bin/bash
set -e
set -o pipefail
set -u

python test_processor.py #unit tests
bash test_plotter.sh #functional test
python plotter.py

pycodestyle test_processor.py
pycodestyle test_plotter.sh
