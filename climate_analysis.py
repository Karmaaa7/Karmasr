# Step 1: Data Loading & Parsing
filename = 'global_warming_dataset.csv'

data = []

with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Get headers from the first line
headers = lines[0].strip().split(',')

# Parse each line
for line in lines[1:]:
    values = line.strip().split(',')
    if len(values) != len(headers):
        continue
    row = dict(zip(headers, values))
    data.append(row)

# ------------Queries-----------

# Query 1: Display the CSV header (column names)
print("CSV Header (Column Names):")
for header in headers:
    print(header)

# Query 2: Count the total number of data records (excluding the header row)
print("Total number of data records (excluding header):", len(data))

# Query 4: Count the number of records for Bangladesh
count_bangladesh = 0
for row in data:
    if row['Country'].strip().lower() == 'bangladesh':
        count_bangladesh += 1
print("Number of records for Bangladesh:", count_bangladesh)

# Query 5: Calculate the average temperature from all the records
total_temp = 0.0
count_temp = 0

for row in data:
    temp_str = row.get('Average_Temperature', '').strip()
    if temp_str != '':
        try:
            total_temp += float(temp_str)
            count_temp += 1
        except ValueError:
            continue

if count_temp > 0:
    avg_temp = total_temp / count_temp
    print("Average temperature from all records:", avg_temp)
else:
    print("No valid temperature data found.")