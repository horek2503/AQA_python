import logging
from definitions import LOGS_FOLDER
from pathlib import Path

debug_log = Path(LOGS_FOLDER, 'debug.log')
error_log = Path(LOGS_FOLDER, 'error.log')

project_logger = logging.getLogger(__name__)
project_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('{asctime} - {levelname}: {message}', style = '{')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(formatter)
project_logger.addHandler(console_handler)

debug_file_handler = logging.FileHandler(filename = debug_log, mode = 'a', encoding='utf-8')
debug_file_handler.setFormatter(formatter)
project_logger.addHandler(debug_file_handler)

error_file_handler = logging.FileHandler(filename = error_log, mode = 'a', encoding='utf-8')
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(formatter)
project_logger.addHandler(error_file_handler)
