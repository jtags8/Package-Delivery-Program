import csv
import datetime


from HashMap import HashMap
from Package import Package
from Truck import Truck


def load_data(filename):
    package_list = []

    with open(filename) as packages:
        package_data = csv.reader(packages, delimiter=',')
        for row in package_data:
            package_list.append(row)
        return package_list

def get_distance(row, column, distances):
    distance = distances[row][column]
    return distance

def get_address_index(address, address_list):
    address_index = address_list.index(address) + 1
    return address_index
def nearest_neighbor(current_address, distances, address_list):

    min_distance = float('inf')
    nearest_address_index = 0

    current_address_index = get_address_index(current_address, address_list)
    for i in range(1, len(address_list)):
        distance = get_distance(current_address_index, i, distances)
        if float(distance) == 0:
            continue

        if float(distance) < float(min_distance):
            min_distance = distance
            nearest_address_index = i

    nearest_address = address_list[nearest_address_index]

    return nearest_address

distances_list = load_data('distances.csv')
addresses_for_distances_list = load_data('addresses_for_distances.csv')
addresses = []
for a in addresses_for_distances_list:
    addresses.append(a[0])


#Test Function for NN
#print(nearest_neighbor("1060 Dalton Ave S", distances_list, addresses))


new_package_list = load_data('Packages.csv')
package_hashmap = HashMap()

for row in new_package_list:
    package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], "at the hub")
    package_hashmap.insert(row[0], package)
    #print(str(package_hashmap.lookup(row[0])))

truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

truck1.load((package_hashmap.get_hash(13), package_hashmap.lookup("13")))
truck1.load((package_hashmap.get_hash(14), package_hashmap.lookup("14")))
truck1.load((package_hashmap.get_hash(15), package_hashmap.lookup("15")))
truck1.load((package_hashmap.get_hash(16), package_hashmap.lookup("16")))
truck1.load((package_hashmap.get_hash(19), package_hashmap.lookup("19")))
truck1.load((package_hashmap.get_hash(20), package_hashmap.lookup("20")))
truck1.load((package_hashmap.get_hash(21), package_hashmap.lookup("21")))
truck1.load((package_hashmap.get_hash(28), package_hashmap.lookup("28")))

truck2.load((package_hashmap.get_hash(1), package_hashmap.lookup("1")))
truck2.load((package_hashmap.get_hash(2), package_hashmap.lookup("2")))
truck2.load((package_hashmap.get_hash(3), package_hashmap.lookup("3")))
truck2.load((package_hashmap.get_hash(4), package_hashmap.lookup("4")))
truck2.load((package_hashmap.get_hash(5), package_hashmap.lookup("5")))
truck2.load((package_hashmap.get_hash(7), package_hashmap.lookup("7")))
truck2.load((package_hashmap.get_hash(8), package_hashmap.lookup("8")))
truck2.load((package_hashmap.get_hash(10), package_hashmap.lookup("10")))
truck2.load((package_hashmap.get_hash(11), package_hashmap.lookup("11")))
truck2.load((package_hashmap.get_hash(12), package_hashmap.lookup("12")))
truck2.load((package_hashmap.get_hash(17), package_hashmap.lookup("17")))
truck2.load((package_hashmap.get_hash(18), package_hashmap.lookup("18")))
truck2.load((package_hashmap.get_hash(36), package_hashmap.lookup("36")))
truck2.load((package_hashmap.get_hash(37), package_hashmap.lookup("37")))
truck2.load((package_hashmap.get_hash(38), package_hashmap.lookup("38")))
truck2.load((package_hashmap.get_hash(40), package_hashmap.lookup("40")))