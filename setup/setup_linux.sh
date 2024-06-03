#!/bin/bash
export $(grep -v '^#' config/config_linux.env | xargs)
