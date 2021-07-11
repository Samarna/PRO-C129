import csv

dataset1 = []
dataset2 = []
with open("final.csv") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)

with open("data_sorted1.csv") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)

headers_1 = dataset1[0]
planet_data1 = dataset1[1:0]
headers_2 = dataset2[0]
planet_data2 = dataset2[1:0]

headers = headers_1+headers_2
planet_data = []
for index,data in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open("combined_data.csv","a+",newline="") as f:
    csv_writer_1 = csv.writer(f)
    csv_writer_1.writerow(headers)
    csv_writer_1.writerows(planet_data)