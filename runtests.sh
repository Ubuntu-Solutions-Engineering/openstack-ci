#!/bin/bash

echo "Starting single install tests ..."
sudo py.test -v -s -r Xf --result-log=/tmp/results.log single
