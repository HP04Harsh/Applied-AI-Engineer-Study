#!/bin/bash

echo "=========================================="
echo "          SYSTEM HEALTH SUMMARY           "
echo "=========================================="

echo -n "Uptime & Load: "
uptime

echo -br "\n--- Memory Usage ---"
free -h

echo -e "\n--- Disk Utilization ---"
df -h --output=source,pcent,target -x tmpfs -x devtmpfs

echo "=========================================="
