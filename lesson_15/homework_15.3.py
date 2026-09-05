import xml.etree.cElementTree as ET
from pathlib import Path
import logging

custom_logger = logging.getLogger(__name__)
custom_logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('{asctime} - {levelname}: {message}', style='{')
console_handler.setFormatter(formatter)
custom_logger.addHandler(console_handler)

current_dir = Path(__file__).parent
source_file = Path(current_dir, 'sources_xml/groups.xml')

tree = ET.parse(str(source_file))
root = tree.getroot()

def get_timingxbytes(group_number:int):
    result = f'No group with number = {group_number}'
    for child in root:
        if child.find('number').text == str(group_number):
            if child.find('timingExbytes') is not None:
                if child.find('timingExbytes').find('incoming') is not None:
                    result = f'For group number {group_number} "timingExbytes" -> "incoming" = {child.find('timingExbytes').find('incoming').text}'
                else:
                    result = f'No "timingExbytes" -> "incoming" for group "{group_number}"'
            else:
                result = f'No "timingExbytes" for group "{group_number}"'
    return result

custom_logger.info(get_timingxbytes(5))
