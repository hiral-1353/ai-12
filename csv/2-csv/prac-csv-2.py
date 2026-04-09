# 8 April
import csv
import os

# Create a file and write some data to it
def create():
    file=open("data.csv", "w", newline="")

    writer=csv.writer(file)
    writer.writerow(["ID","Name","Class"])
    writer.writerow(["1","John","10"])
    writer.writerow(["2","Jane","11"])

    file.close()

    print("File created")

# 9 April
# Delete record
def delete():
    file=open("data.csv", "r")
    reader=csv.reader(file)
    
    temp_file=open("temp.csv", "w", newline="")
    writer=csv.writer(temp_file)

    delete_name = input("Enter the name to delete: ")

    found = False

    for row in reader:
        if row[0] == "ID":
            writer.writerow(row)
            continue

        if row[1].lower() == delete_name.lower():
            found = True
            continue

        else:
            writer.writerow(row)
        
        file.close()
        temp_file.close()

        os.remove("students.csv")
        os.rename("temp.csv", "students.csv")  

        if found:
            print(f"{delete_name} has been deleted.")
        else:
            print(f"{delete_name} not found in the file.") 

create()
delete()