import json
import csv
from pathlib import Path

current_folder = Path(__file__).parent
json_folder = Path(current_folder, 'jsons')
csv_folder = Path(current_folder, 'csvs')

json_folder.mkdir(exist_ok=True)
csv_folder.mkdir(exist_ok=True)
input_json_file = Path(json_folder, 'persons.json')
output_csv_file = Path(csv_folder, 'persons.csv')

with open(input_json_file,'r+') as file:
    persons = json.load(file)

persons_as_tuples = []
persons_set = set()
for person in persons:
    persons_as_tuples.append(tuple(person.items()))
persons_set = set(persons_as_tuples)

print(unique_persons[0])
# print(persons[0])

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