#!/usr/bin/env bash

zip -r solution.zip ./javascript/ ./python/ ./sql/ || exit 1;
echo "solution.zip ready";
