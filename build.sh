#!/bin/bash

python3 clean_refs.py
python3 add_consortium.py
jupyter-book clean --html docs
jupyter-book build docs
python3 clean_consortium.py
