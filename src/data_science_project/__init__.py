##set up logging for data science project 
import logging
import os
import sys
from pathlib import Path
logging_str="[%(asctime)s]: %(levelname)s: %(module)s: %(message)s"
logs_dir="logs"
log_filepath=os.path.join(logs_dir,"logging.log")
os.makedirs(logs_dir,exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)])
logger=logging.getLogger("datasciencelogger")

