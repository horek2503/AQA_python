from homework_13 import log_event
import pytest
import logging

log_file_name = 'login_system.log'


def read_log_last_line(filename):
    with open(filename) as file:
        return file.readlines()[-1]


@pytest.mark.parametrize('username, status',
                         [('user1', 'success'),
                          ('user2', 'expired'),
                          ('user3', 'failed')])
def test_log_event_functional(username, status):
    log_event(username, status)
    last_log_record = read_log_last_line(log_file_name).strip()
    expected_message_ending = f"Login event - Username: {username}, Status: {status}"
    assert last_log_record.endswith(expected_message_ending), f'User "{username}" with status "{status}" is not logged!'


@pytest.mark.parametrize('username, status, expected_log_level',
                         [('Andrii', 'success', 'INFO'),
                          ('Olena', 'expired', 'WARNING'),
                          ('Stepan', 'failed', 'ERROR'),
                          ('', '', 'ERROR'),
                          ('Iryna', None, 'ERROR'),
                          ('Maryna', 90, 'ERROR')
                          ])
def test_log_event_check_log_level_is_correct(username, status, expected_log_level):
    log_event(username, status)
    last_log_record = read_log_last_line(log_file_name)
    assert (expected_log_level in last_log_record), f'Incorrect log level for user "{username}" with status "{status}": expected level = "{expected_log_level}"'
