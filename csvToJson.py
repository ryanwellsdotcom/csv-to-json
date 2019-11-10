import csv
import json

with open('sample.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('sample.json', 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)
