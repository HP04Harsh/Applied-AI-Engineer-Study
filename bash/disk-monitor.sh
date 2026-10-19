#!/bin/bash

# Root partition ka disk usage percentage nikalna
USAGE=$(df / | grep / | awk '{print $5}' | sed 's/%//g')

THRESHOLD=80

if [ "$USAGE" -gt "$THRESHOLD" ]; then
    echo "WARNING: Disk usage is high! Current usage is: ${USAGE}%"
else
    echo "Disk space is normal. Current usage is: ${USAGE}%"
fi
