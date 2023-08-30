import csv
import datetime


from HashMap import HashMap
from Package import Package
from Truck import Truck


def load_data(filename):
    package_list = []

    with open(filename) as packages:
        package_data = csv.reader(packages, delimiter=',')
        next(package_data) #skips the header
        for row in package_data:
            package_list.append(row)
        return package_list
def nearest_neighbor(current_address, distances, addresses):

    min_distance = float('inf')
    nearest_address = None

    address_index = addresses.index(current_address)
    address_distance_list = distances[address_index]
    for d in address_distance_list:
        if d == 0.0:
            continue

        if d == '':
            address_index -= 1
            address_distance_list += 1
            if float(address_distance_list[address_index]) < float(min_distance):
                min_distance = address_distance_list[address_index]

        #if float(d) < float(min_distance):
        #    min_distance = d

    #nearest_address_index = address_distance_list.index(d)
    #nearest_address = addresses[nearest_address_index]

    return min_distance

distances_list = load_data('distances.csv')
addresses_for_distances_list = load_data('addresses_for_distances.csv')
addresses = []
for a in addresses_for_distances_list:
    addresses.append(a[0])
print(addresses)
print(nearest_neighbor("1060 Dalton Ave S", distances_list, addresses))


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