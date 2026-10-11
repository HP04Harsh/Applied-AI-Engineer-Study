#!/bin/bash

read -p "Enter username to check: " USERNAME

if grep -q "^$USERNAME:" /etc/passwd; then
    echo "User '$USERNAME' exists on this system."
else
    echo "User '$USERNAME' does not exist."
fi
