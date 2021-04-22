import csv

csv_rows = ["id", "description", "completed", "dueDate"]

# Specify the exact location of the db.csv file in your case.
file_dir = "/home/vivek/Documents/Projects/Python/python-gql-demo/python-gql-demo/api/db.csv"


# This function converts the csv data row into a dictionary
def line_to_obj(line):
    line_dict = {
        "id": line[0],
        "description": line[1],
        "completed": line[2],
        "dueDate": line[3]
    }
    return line_dict


# This function retreves the csv data from the file and returns the list of dictionaries
def csv_to_dict():
    firstLine = True
    dict_list = []
    with open(file_dir, 'r') as data:
        for line in csv.reader(data):
            if firstLine:
                firstLine = False
                continue
            dict_list.append(line_to_obj(line))
    return dict_list


# This function  stores the modified data to the csv file
def dict_to_csv(data):
    with open(file_dir, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_rows)
        writer.writeheader()
        writer.writerows(data)
