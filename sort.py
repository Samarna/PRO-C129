import csv

data = []
with open("data.csv") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers = data[0]
planet_data = data[1:]
for data_point in planet_data:
    data_point[0] = data_point[0].lower()

planet_data.sort(key=lambda planet_data:planet_data[0])
with open("data_sorted1.csv","a+",newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)