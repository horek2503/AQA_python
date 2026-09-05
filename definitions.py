from pathlib import Path

BASE_FOLDER = Path(__file__).parent
TEMP_FOLDER = BASE_FOLDER / 'temp'
UTILS_FOLDER = Path(BASE_FOLDER ,'utils')
LOGS_FOLDER = Path(BASE_FOLDER, 'logs')

TEMP_FOLDER.mkdir(exist_ok=True)
LOGS_FOLDER.mkdir(exist_ok=True)
