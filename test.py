import csv
from tabulate import tabulate as tb
import pandas as pd

jadwal = []
with open('jadwal_pesawat.csv', 'r') as file:
    reader = csv.DictReader(file)
    table = tb(jadwal, headers="firstrow", tablefmt="grid")
    for row in file:
        jadwal.append(row)
        
print(jadwal)

df = pd.DataFrame(jadwal)
print(df)

print(table)