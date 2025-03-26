"""
    Logging
"""
import logging

# Setting log
logging.basicConfig(
    level=logging.INFO,  # Write log INFO
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format log
    handlers=[
        logging.FileHandler("app.log"),  # Write to file app.log
    ]
)

# Create logger
logger = logging.getLogger(__name__)
