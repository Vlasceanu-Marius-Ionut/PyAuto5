import os
import shutil
import tempfile
from pathlib import Path
import time

# Folders to clean
folders = [
    Path(tempfile.gettempdir()),      # User temporary folder
    Path(os.environ.get('TEMP')),     # %TEMP% folder
    Path("C:/Windows/Prefetch")       # Prefetch folder
]

def clean_folders():
    """Delete all files and folders possible, skip locked items"""
    for folder in folders:
        if folder.exists():
            for item in folder.iterdir():
                try:
                    if item.is_file():
                        item.unlink()      # Delete file
                    else:
                        shutil.rmtree(item) # Delete folder and its contents
                except Exception:
                    pass  # Ignore locked files/folders

# Run cleanup
clean_folders()

print("Cleanup done :)")

# Countdown before exit
for i in range(1, 4):
    print("Exiting in:", i)
    time.sleep(1)
