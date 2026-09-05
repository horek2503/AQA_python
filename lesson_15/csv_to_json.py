import csv
import json
from pathlib import Path
from definitions import BASE_FOLDER

input_file = Path(BASE_FOLDER, 'temp/output_persons.csv')
output_file = Path(BASE_FOLDER, 'temp/output_persons.json')

with open(input_file, mode='r', encoding='utf-8') as file:
    reader = list(csv.reader(file))

headers = tuple(reader[0])
body = reader[1:]
output_data = list()

# make dict from each person data
for person in body:
    person_tuple = tuple(person)
    person_data = dict(zip(headers, person_tuple))
    output_data.append(person_data)

### Option 1 - change '' values -> None
# for index in range(len(output_data)):
#     if '' in output_data[index].values():
#          output_data[index] = {key:
#                   value if value != '' else None
#               for key, value in output_data[index].items()}

### Option 2 - skip '' values
for index in range(len(output_data)):
    if '' in output_data[index].values():
        new_person_dict = dict()
        for key, value in output_data[index].items():
            if not value == '':
                new_person_dict[key] = value
            else:
                continue
        output_data[index] = new_person_dict

with open(output_file, mode = 'w') as file:
    json.dump(output_data, file, indent=4)