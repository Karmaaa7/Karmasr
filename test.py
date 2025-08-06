import csv
from collections import defaultdict

# Step 1: Data Loading & Parsing
filename = 'global_warming_dataset.csv'

data = []

with open(filename, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Print the number of rows loaded and the first row as a sample
print(f"Total records loaded: {len(data)}")
print("First record:")
print(data[0])

# Function 1: Earliest and Latest Year in Dataset
def get_year_range(data):
    years = []
    for row in data:
        try:
            years.append(int(row['Year']))
        except:
            continue
    if years:
        return min(years), max(years)
    else:
        return None, None

# Function 2: Min and Max Solar Energy Potential
def get_solar_energy_range(data):
    values = []
    for row in data:
        try:
            values.append(float(row['Solar_Energy_Potential']))
        except:
            continue
    if values:
        return min(values), max(values)
    else:
        return None, None

# Function 3: Top 3 Countries by Forest Area
def get_top_forest_countries(data, top_n=3):
    forest_data = []
    for row in data:
        try:
            forest_area = float(row['Forest_Area'])
            country = row['Country']
            forest_data.append((country, forest_area))
        except:
            continue
    forest_data.sort(key=lambda x: x[1], reverse=True)
    return forest_data[:top_n]

# Query 1
min_year, max_year = get_year_range(data)
print("\nEarliest year in dataset:", min_year)
print("Latest year in dataset:", max_year)

# Query 2
min_solar, max_solar = get_solar_energy_range(data)
print("\nMinimum Solar Energy Potential:", min_solar)
print("Maximum Solar Energy Potential:", max_solar)

# Query 3
top_forest = get_top_forest_countries(data)
print("\nTop 3 countries by forest area percentage:")
for country, area in top_forest:
    print(f"{country}: {area:.2f}%")