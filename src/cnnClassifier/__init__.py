import logging  # Import the logging module to handle logging in the application
import os       # Import os module to handle directory and file operations
import sys      # Import sys module to interact with the system

# Define the logging format to include timestamp, log level, module name, and message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory where log files will be stored
log_dir = "logs"

# Define the file path for storing logs inside the log directory
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it does not already exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO (captures INFO, WARNING, ERROR, CRITICAL)
    format=logging_str,  # Use the defined logging format
    
    handlers=[
        logging.FileHandler(log_filepath),  # Log messages to the specified file
        logging.StreamHandler(sys.stdout)   # Print log messages to the console
    ]
)

# Create a logger instance named 'nnClassifierLogger'
logger = logging.getLogger("nnClassifierLogger")
