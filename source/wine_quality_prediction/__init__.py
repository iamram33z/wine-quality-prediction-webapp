# Import Libraries
import os
import sys
import logging

# Define the logging String
logging_str = "[%(asctime)s - %(name)s - %(levelname)s - %(message)s}"

# Define the logging directory
logging_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
logging_file = os.path.join(logging_dir, "running_logs.log")
os.makedirs(logging_dir, exist_ok=True)

# Define the logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(logging_file),
        logging.StreamHandler(sys.stdout)
    ]
)

# Define the logger
logger = logging.getLogger(__name__)