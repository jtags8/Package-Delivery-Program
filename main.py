import csv

def load_data(filename):
    package_list = []

    with open(filename) as packages:
        package_data = csv.reader(packages, delimiter=',')
        next(package_data) #skips the header
        for row in package_data:
            package_list.append(row)
        return package_list

new_package_list = load_data('Packages.csv')
for row in new_package_list:
    print(row)