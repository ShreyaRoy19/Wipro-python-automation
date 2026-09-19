import csv
import os

def load_csv_data(file_name):
    rows = []
    file_path = os.path.join(os.path.dirname(__file__), '..', 'csv_data', file_name)
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows