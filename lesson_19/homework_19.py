import logging
from datetime import datetime, timedelta

heartbeat_source_file = 'hblog.txt'
heartbeat_log_file = 'hb_test.log'
heartbeat_warning_threshold_sec = 31
heartbeat_error_threshold_sec = 33

hw_19_logger = logging.getLogger()
hw_19_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(filename=heartbeat_log_file, mode='w', encoding='utf-8')
file_formatter = logging.Formatter('{levelname}: {message}', style='{')
file_handler.setFormatter(file_formatter)
hw_19_logger.addHandler(file_handler)

filtered_heartbeat_records = []
target_identifier = 'Key TSTFEED0300|7E3E|0400'

with open(heartbeat_source_file, mode='r') as file:
    for line in file:
        if target_identifier in line:
            filtered_heartbeat_records.append(line)


def log_exceed_heartbeat_time_limit(heartbeat_records: list, warn_threshold: int, err_threshold: int, log_file: str):
    timestamp_position_in_log_record = heartbeat_records[0].split().index('Timestamp') + 1

    for index in range(len(heartbeat_records) - 1):
        split_line_current = heartbeat_records[index].split()
        split_line_next = heartbeat_records[index + 1].split()

        current_time_str = split_line_current[timestamp_position_in_log_record]
        next_time_str = split_line_next[timestamp_position_in_log_record]

        current_time = datetime.strptime(current_time_str, '%H:%M:%S')
        next_time = datetime.strptime(next_time_str, '%H:%M:%S')

        time_diff = max(next_time, current_time) - min(next_time, current_time)

        if time_diff >= timedelta(seconds=err_threshold):
            hw_19_logger.error(
                f'Line {index}: Difference between time records "{current_time_str}" and "{next_time_str}" is "{time_diff}"')
            continue

        if time_diff > timedelta(seconds=warn_threshold):
            hw_19_logger.warning(
                f'Line {index}:Difference between time records "{current_time_str}" and "{next_time_str}" is "{time_diff}"')
            continue


log_exceed_heartbeat_time_limit(filtered_heartbeat_records, heartbeat_warning_threshold_sec,
                                heartbeat_error_threshold_sec, heartbeat_log_file)
