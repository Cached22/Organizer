import logging
import os
from logging.handlers import RotatingFileHandler

# Define the base directory for log files
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Define the log file path
LOG_FILE_PATH = os.path.join(LOG_DIR, 'space_organizer.log')

# Create a custom logger
logger = logging.getLogger('space_organizer_logger')
logger.setLevel(logging.INFO)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=10240, backupCount=3)

# Create formatters and add it to handlers
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(log_format)
file_handler.setFormatter(log_format)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def log_event(message, level=logging.INFO):
    """
    Log an event at the specified level.
    :param message: str, the message to log
    :param level: logging level, e.g., logging.INFO, logging.ERROR
    """
    if level == logging.INFO:
        logger.info(message)
    elif level == logging.WARNING:
        logger.warning(message)
    elif level == logging.ERROR:
        logger.error(message)
    elif level == logging.DEBUG:
        logger.debug(message)
    else:
        logger.log(level, message)

def log_error(message):
    """
    Log an error message.
    :param message: str, the error message to log
    """
    logger.error(message)

# Example usage:
# log_event("This is an info message")
# log_error("This is an error message")