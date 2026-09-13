import json
from pathlib import Path
from utils.logger_tool import project_logger

current_folder = Path(__file__).parent
sources_folder = Path(current_folder, 'sources_json')

json_files = [file for file in sources_folder.iterdir() if file.is_file() and file.suffix == '.json']

for file in json_files:
    path_to_file = Path(sources_folder, file)
    with open(path_to_file, 'r', encoding="utf-8") as f:
        try:
            file_data = json.load(f)
        except Exception:
            project_logger.error(f"File is not a valid JSON: {path_to_file}")
        else:
            project_logger.info(f"JSON file opened successfully: {path_to_file}")
