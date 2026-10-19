#!/bin/bash

# Source directory aur Backup destination define karo
SOURCE_DIR="/home/user/my_project"
BACKUP_DIR="/home/user/backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_NAME="project_backup_$TIMESTAMP.tar.gz"

# Check karo ki backup folder exist karta hai ya nahi
if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
fi

# Tar command se backup create karo
tar -czf "$BACKUP_DIR/$BACKUP_NAME" "$SOURCE_DIR"

echo "Backup successfully created: $BACKUP_NAME"
