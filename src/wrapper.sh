#!/bin/bash
# wrapper.sh

# Set up the environment variables
export CHROMEDRIVER_PATH=/home/xo/Desktop/VScodeProjects/WhatsappAuto2/chromedriver-linux64/chromedriver
export CHROME_BINARY_PATH=/usr/bin/google-chrome
export CHROME_USER_DATA_DIR=/home/xo/Desktop/VScodeProjects/WhatsappAuto2/ChromeProfile


# Run the Python script
/home/xo/miniconda3/bin/python /path/to/your/script.py "$1" "$2"
