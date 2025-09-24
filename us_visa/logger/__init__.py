import logging
import os 
from from_root import from_root
from datetime import datetime

LOG_FILE_NAME = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

log_dir = "logs"

log_path = os.path.join(from_root(), log_dir, LOG_FILE_NAME)

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s]%(name)s -  %(levelname)s - %(message)s",
    level=logging.DEBUG,
)