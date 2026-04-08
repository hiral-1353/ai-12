import csv

# Create a file and write some data to it
def create():
    file=open('data.csv', 'w', newline='')

    writer=csv.writer(file)
    writer.writerow(['ID','Name','Class'])
    writer.writerow(['1','John','10'])
    writer.writerow(['2','Jane','11'])

    file.close()

    print("File created")
    