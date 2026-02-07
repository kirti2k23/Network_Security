import logging
import os
from pathlib import Path
from datetime import datetime

"""
This script will do logging and save logs in log folder

"""

log_dir = "Logs"
os.makedirs(log_dir,exist_ok=True)

log_file = f"logs{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

log_file_path = os.path.join(log_dir,log_file)

# Configuration of logging

logger = logging.getLogger("NetworkSecurityLogs")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s %(name)s - %(message)s"
)

file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

if __name__ == "__main__":
    logger.info("Checking logging script")