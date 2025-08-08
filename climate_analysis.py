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

# Step 2: Define Queries
def query_1():
    print("CSV Header (Column Names):")
    for header in headers:
        print(header)

def query_2():
    print("Total number of data records (excluding header):", len(data))

def query_3():
    print("All records from the year 2020:")
    for row in data:
        if row.get('Year', '').strip() == '2020':
            print(row)

def query_4():
    count_bangladesh = sum(1 for row in data if row.get('Country', '').strip().lower() == 'bangladesh')
    print("Number of records for Bangladesh:", count_bangladesh)

def query_5():
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

def query_6():
    max_co2 = None
    for row in data:
        try:
            co2 = float(row.get('CO2_Emissions', '').strip())
            if max_co2 is None or co2 > max_co2:
                max_co2 = co2
        except ValueError:
            continue
    print("Maximum CO₂ emission value:", max_co2)

def query_7():
    print("Years where average temperature was greater than 30°C:")
    years = set()
    for row in data:
        try:
            temp = float(row.get('Average_Temperature', '').strip())
            if temp > 30:
                years.add(row.get('Year', '').strip())
        except ValueError:
            continue
    for year in sorted(years):
        print(year)

def query_8():
    print("Countries where sea level is greater than 3 meters:")
    countries = set()
    for row in data:
        try:
            sea = float(row.get('Sea_Level', '').strip())
            if sea > 3:
                countries.add(row.get('Country', '').strip())
        except ValueError:
            continue
    for country in sorted(countries):
        print(country)

def query_9():
    print("Population of India for each year:")
    for row in data:
        if row.get('Country', '').strip().lower() == 'india':
            print(f"Year: {row.get('Year', '').strip()}, Population: {row.get('Population', '').strip()}")

def query_10():
    countries = set(row.get('Country', '').strip() for row in data if row.get('Country', '').strip())
    print("Number of unique countries:", len(countries))

def query_11():
    print("Top 5 records with highest CO₂ emission values:")
    sorted_data = sorted(
        [row for row in data if row.get('CO2_Emissions', '').strip() != ''],
        key=lambda x: float(x['CO2_Emissions']), reverse=True
    )
    for row in sorted_data[:5]:
        print(row)

def query_12():
    print("All data between the years 2010 and 2015:")
    for row in data:
        try:
            year = int(row.get('Year', '').strip())
            if 2010 <= year <= 2015:
                print(row)
        except ValueError:
            continue

def query_13():
    print("Countries with population greater than 1 billion:")
    countries = set()
    for row in data:
        try:
            pop = float(row.get('Population', '').strip())
            if pop > 1_000_000_000:
                countries.add(row.get('Country', '').strip())
        except ValueError:
            continue
    for country in sorted(countries):
        print(country)

def query_14():
    years = set(row.get('Year', '').strip() for row in data if row.get('Year', '').strip())
    print("Number of unique years:", len(years))

def query_15():
    min_temp = None
    min_row = None
    for row in data:
        try:
            temp = float(row.get('Average_Temperature', '').strip())
            if min_temp is None or temp < min_temp:
                min_temp = temp
                min_row = row
        except ValueError:
            continue
    print("Record with lowest average temperature:", min_row)

def query_16():
    print("Top 10 hottest years based on average temperature:")
    year_temp = {}
    for row in data:
        try:
            year = row.get('Year', '').strip()
            temp = float(row.get('Average_Temperature', '').strip())
            if year not in year_temp or temp > year_temp[year]:
                year_temp[year] = temp
        except ValueError:
            continue
    for year, temp in sorted(year_temp.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"Year: {year}, Temp: {temp}")

def query_17():
    print("Top 10 countries with highest CO₂ emissions:")
    country_co2 = {}
    for row in data:
        try:
            country = row.get('Country', '').strip()
            co2 = float(row.get('CO2_Emissions', '').strip())
            if country not in country_co2 or co2 > country_co2[country]:
                country_co2[country] = co2
        except ValueError:
            continue
    for country, co2 in sorted(country_co2.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"Country: {country}, CO₂: {co2}")

def query_18():
    print("Bottom 5 coldest years based on average temperature:")
    year_temp = {}
    for row in data:
        try:
            year = row.get('Year', '').strip()
            temp = float(row.get('Average_Temperature', '').strip())
            if year not in year_temp or temp < year_temp[year]:
                year_temp[year] = temp
        except ValueError:
            continue
    for year, temp in sorted(year_temp.items(), key=lambda x: x[1])[:5]:
        print(f"Year: {year}, Temp: {temp}")

def query_19():
    print("Top 10 records with highest sea level values:")
    sorted_data = sorted(
        [row for row in data if row.get('Sea_Level', '').strip() != ''],
        key=lambda x: float(x['Sea_Level']), reverse=True
    )
    for row in sorted_data[:10]:
        print(row)

def query_20():
    print("Top 10 most populous countries based on population:")
    country_pop = {}
    for row in data:
        try:
            country = row.get('Country', '').strip()
            pop = float(row.get('Population', '').strip())
            if country not in country_pop or pop > country_pop[country]:
                country_pop[country] = pop
        except ValueError:
            continue
    for country, pop in sorted(country_pop.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"Country: {country}, Population: {pop}")

query_functions = [
    None, query_1, query_2, query_3, query_4, query_5, query_6, query_7, query_8, query_9, query_10,
    query_11, query_12, query_13, query_14, query_15, query_16, query_17, query_18, query_19, query_20
]

def print_menu():
    print("\nSelect a query to run (1-20):")
    print(" 1. Display the CSV header (column names)")
    print(" 2. Count the total number of data records (excluding header)")
    print(" 3. Show all records from the year 2020")
    print(" 4. Count the number of records for Bangladesh")
    print(" 5. Calculate the average temperature from all records")
    print(" 6. Find the maximum CO₂ emission value in the dataset")
    print(" 7. List all years where average temperature was greater than 30°C")
    print(" 8. List all countries where sea level is greater than 3 meters")
    print(" 9. Show population of India for each year (if available)")
    print("10. Count how many unique countries are present in the dataset")
    print("11. Display the top 5 records with the highest CO₂ emission values")
    print("12. Show all data between the years 2010 and 2015")
    print("13. List all countries with a population greater than 1 billion")
    print("14. Count the number of unique years in the dataset")
    print("15. Display the record with the lowest average temperature")
    print("16. Show the top 10 hottest years based on average temperature")
    print("17. List the top 10 countries with the highest CO₂ emissions")
    print("18. Show the bottom 5 coldest years based on average temperature")
    print("19. List the top 10 records with the highest sea level values")
    print("20. List the top 10 most populous countries based on population")
    print(" 0. Exit")

while True:
    print_menu()
    try:
        choice = int(input("Enter your choice (0-20): "))
        if choice == 0:
            print("Exiting.")
            break
        elif 1 <= choice <= 20:
            query_functions[choice]()
            cont = input("\nPress Enter to continue or 0 to exit: ")
            if cont.strip() == "0":
                print("Exiting.")
                break
        else:
            print("Invalid choice. Please enter a number between 0 and 20.")
    except ValueError:
        print("Invalid input. Please enter a number.")