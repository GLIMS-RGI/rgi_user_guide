#!/bin/bash

echo "Building v7.1"
python3 clean_refs.py
python3 add_consortium.py
jupyter-book clean --html docs
jupyter-book build docs
python3 clean_consortium.py
