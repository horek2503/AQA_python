from definitions import BASE_FOLDER
from pathlib import Path
import json
import csv

input_file = Path(BASE_FOLDER, 'temp/persons.json')
output_file = Path(BASE_FOLDER, 'temp/output_persons.csv')

with open(input_file, mode='r', encoding='utf-8') as file:
    input_data = json.load(file)

headers = list()
for person in input_data:
    for person_key in person.keys():
        if person_key not in headers:
            headers.append(person_key)

body = list()
for person in input_data:
    person_data = [person.get(key, '') for key in headers]
    body.append(person_data)
print(headers)
print(body)

with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(body)


#
# rows_as_tuples = [tuple(x) for x in rows]
# unique_rows = set(rows_as_tuples)
#
# print(len(rows))
# print(len(unique_rows))
#
# output_data = list(headers)
# output_data = output_data.app
# print(output_data)

# file_data_dict = [dict(zip(headers, row)) for row in rows]
# print(file_data_dict)


#
#
# json_folder = Path(current_folder, 'jsons')
# csv_folder = Path(current_folder, 'csvs')
# json_folder.mkdir(exist_ok=True)
# csv_folder.mkdir(exist_ok=True)
# input_json_file = Path(json_folder, 'persons.json')
# output_csv_file = Path(csv_folder, 'persons.csv')
#
# with open(input_json_file,'r+') as file:
#     persons = json.load(file)
#
# persons_as_tuples = []
# persons_set = set()
# for person in persons:
#     persons_as_tuples.append(tuple(person.items()))
# persons_set = set(persons_as_tuples)
#
# result_list = []
# for person in persons_set:
#     result_list.append(dict(person))
#
# print(result_list)

# print(persons_set)
# keys = [x for x in persons[0].keys()]
# persons_output = [keys]
# for person in persons:
#     values = []
#     for key in keys:
#         values.append(person[key])
#     persons_output.append(values)
#
# with open(output_csv_file, 'w+', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(persons_output)