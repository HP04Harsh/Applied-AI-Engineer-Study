#!/bin/bash

while true; do
    echo "=== SYSTEM INFO MENU ==="
    echo "1. Check Uptime"
    echo "2. Check Memory Usage"
    echo "3. Exit"
    read -p "Choose an option (1-3): " choice

    case $choice in
        1)
            uptime
            ;;
        2)
            free -h
            ;;
        3)
            echo "Exiting..."
            break
            ;;
        *)
            echo "Invalid option, please try again."
            ;;
    esac
    echo ""
done
