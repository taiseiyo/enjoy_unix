#!/bin/bash

url=$(python3 fetch_qiita.py)

firefox $url
