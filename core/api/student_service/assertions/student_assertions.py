from datetime import datetime, timezone

class StudentAssertBase:

    def check_student_response_structure(self, student):
        datetime_format = '%Y-%m-%dT%H:%M:%S%z'

        assert student['id'] != 0
        assert len(student['name']) > 0
        assert 0 < student['score'] <= 100
        assert len(student['score_name']) > 0
        assert student['created_date'] > 0
        assert (datetime.strptime(student['updated_date'], datetime_format).astimezone(timezone.utc)
                < datetime.now(timezone.utc))

    def check_students_are_sorted_by_param(self, students: list, sorting_param):
        is_reverse_sorting = sorting_param.startswith('-')
        sorted_students = sorted(students, key=lambda x: x[sorting_param.lstrip('-')], reverse=is_reverse_sorting)
        assert sorted_students == students, f'Sorting failed by {sorting_param}'