import os
import pytest
from loguru import logger
from datetime import datetime


def loguru_conf(test_name):
    logs_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Logs")
    os.makedirs(logs_directory, exist_ok=True)

    log_file = os.path.join(logs_directory, f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {test_name}.log")
    logger.add(log_file, level="INFO")
