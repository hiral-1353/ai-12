import csv
import os
 
# Step 1: Create file with sample data
def create_file():
    file = open("students.csv", "w", newline="")
    writer = csv.writer(file)
 
    writer.writerow(["ID", "Name", "Marks"])
    writer.writerow([1, "John", 89])
    writer.writerow([2, "Jane", 90])
    writer.writerow([3, "Mike", 79])
    
    file.close()
    print("File created successfully.\n")
 
 
# Step 2: Delete record function
def delete_record():
    file = open("students.csv", "r")
    reader = csv.reader(file)
 
    temp_file = open("temp.csv", "w", newline="")
    writer = csv.writer(temp_file)
 
    delete_name = input("Enter name to delete: ")
 
    found = False
 
    for row in reader:
        # Keep header as it is
        if row[0] == "ID":
            writer.writerow(row)
            continue
 
        # If record matches → skip (delete)
        if row[1].lower() == delete_name.lower():
            found = True
            continue
        else:
            writer.writerow(row)
 
    file.close()
    temp_file.close()
 
    # Replace original file with updated file
    os.remove("students.csv")
    os.rename("temp.csv", "students.csv")
 
    if found:
        print("\nRecord deleted successfully.")
    else:
        print("\nRecord not found.")
 
 
# Step 3: Main Program
create_file()
delete_record()