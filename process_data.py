# Convert three data csv files into one csv containing: Sales, Date and Region


#Use os package to get all files in data directory
import os


# clean all data in given file and append to 'clean_data.csv'
def prepare_data(filepath):

    # clear new_data each time funcion is called as to not add the same data to csv
    new_data = []
    with open(filepath) as readfile:
        data = readfile.readlines()

        #Filter out any non pink morsel entries and add data for new file to new data list
        for line in data:
            line = line.split(",")
            if line[0] == "pink morsel":
                cost = float(line[1][1:])
                quantity = float(line[2])
                sale = cost * quantity
                date, region = line[3], line[4].strip()
                new_data.append(f"{sale}, {date}, {region}")

    # add contents of new data list to 'clean_data.csv'
    with open("clean_data.csv", "a") as writefile:
        for entry in new_data:
            writefile.write(entry + "\n")


# Add header to csv
with open("clean_data.csv", "a") as writefile:
    writefile.write("sales,date,region" + "\n")

# run through all files and call prepare_data
for file in os.scandir("data"):
    prepare_data(file)