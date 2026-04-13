# 7 April
import csv
import os

data = [
    ["S. No.","Name","Class"],
    [1, "A", "XI"],
    [2, "B", "XI"],
    [3, "C", "XI"],
    [4, "D", "XI"]
]

# Create a CSV file and write the data to it
with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created")

# Read the CSV file and print its contents
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# 8 April

# Append a new row to the CSV file
ndata = [5,"E","XI"]
with open("students.csv","a",newline="") as file:
  writer = csv.writer(file)
  writer.writerow(ndata)
  
print("Updated")

#os.rename("students.csv","list.csv")