import csv
from pathlib import Path

current_folder = Path(__file__).parent
sources_folder = Path(current_folder, 'sources_csv')
targets_folder = Path(current_folder, 'results')

file1 = Path(sources_folder, 'r-m-c.csv')
file2 = Path(sources_folder, 'rmc.csv')
result_file = Path(targets_folder, 'result_bocharov.csv')

with open(file1, 'r', newline='') as file:
    file1_data = list(csv.reader(file))

with open(file2, 'r', newline='') as file:
    file2_data = list(csv.reader(file,delimiter=';'))

file1_headers = file1_data[0]
file2_headers = file2_data[0]
file1_rows = file1_data[1:]
file2_rows = file2_data[1:]
combined_rows = file1_rows.copy()
combined_rows.extend(file2_rows)

unique_set = set([tuple(x) for x in combined_rows])
result_data = [list(x) for x in unique_set]

with open(result_file, mode = 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(file1_headers)
    writer.writerows(result_data)
