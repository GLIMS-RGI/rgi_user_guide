#!/bin/bash

python3 clean_refs.py
jupyter-book clean --html docs
jupyter-book build docs
