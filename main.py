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
def nearest_neighbor(current_address, truck_packages, distances, address_list):

    min_distance = float('inf')
    nearest_address_index = 0

    current_address_index = get_address_index(current_address, address_list)
    for index in truck_packages:
        distance = get_distance(current_address_index, index, distances)
        if float(distance) == 0:
            continue

        if float(distance) < float(min_distance):
            min_distance = distance
            nearest_address_index = index

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
    print(str(package_hashmap.lookup(row[0])))

truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

#package_hashmap.lookup("1")

#Load all 3 trucks
truck1.load(1)
truck1.load(4)
truck1.load(13)
truck1.load(14)
truck1.load(15)
truck1.load(16)
truck1.load(19)
truck1.load(20)
truck1.load(34)
truck2.load((package_hashmap.get_hash(2), package_hashmap.lookup("2")))
truck2.load((package_hashmap.get_hash(3), package_hashmap.lookup("3")))
truck2.load((package_hashmap.get_hash(5), package_hashmap.lookup("5")))
truck2.load((package_hashmap.get_hash(7), package_hashmap.lookup("7")))
truck2.load((package_hashmap.get_hash(8), package_hashmap.lookup("8")))
truck2.load((package_hashmap.get_hash(10), package_hashmap.lookup("10")))
truck2.load((package_hashmap.get_hash(18), package_hashmap.lookup("18")))
truck2.load((package_hashmap.get_hash(22), package_hashmap.lookup("22")))
truck2.load((package_hashmap.get_hash(24), package_hashmap.lookup("24")))
truck2.load((package_hashmap.get_hash(29), package_hashmap.lookup("29")))
truck2.load((package_hashmap.get_hash(30), package_hashmap.lookup("30")))
truck2.load((package_hashmap.get_hash(33), package_hashmap.lookup("33")))
truck2.load((package_hashmap.get_hash(36), package_hashmap.lookup("36")))
truck2.load((package_hashmap.get_hash(37), package_hashmap.lookup("37")))
truck2.load((package_hashmap.get_hash(38), package_hashmap.lookup("38")))
truck3.load((package_hashmap.get_hash(6), package_hashmap.lookup("6")))
truck3.load((package_hashmap.get_hash(9), package_hashmap.lookup("9")))
truck3.load((package_hashmap.get_hash(11), package_hashmap.lookup("11")))
truck3.load((package_hashmap.get_hash(12), package_hashmap.lookup("12")))
truck3.load((package_hashmap.get_hash(17), package_hashmap.lookup("17")))
truck3.load((package_hashmap.get_hash(21), package_hashmap.lookup("21")))
truck3.load((package_hashmap.get_hash(23), package_hashmap.lookup("23")))
truck3.load((package_hashmap.get_hash(25), package_hashmap.lookup("25")))
truck3.load((package_hashmap.get_hash(26), package_hashmap.lookup("26")))
truck3.load((package_hashmap.get_hash(27), package_hashmap.lookup("27")))
truck3.load((package_hashmap.get_hash(28), package_hashmap.lookup("28")))
truck3.load((package_hashmap.get_hash(31), package_hashmap.lookup("31")))
truck3.load((package_hashmap.get_hash(32), package_hashmap.lookup("32")))
truck3.load((package_hashmap.get_hash(35), package_hashmap.lookup("35")))
truck3.load((package_hashmap.get_hash(39), package_hashmap.lookup("39")))
truck3.load((package_hashmap.get_hash(40), package_hashmap.lookup("40")))

#Create three lists for 8:00, 9:05, and 10:20
#for loop to iterate through all packages, change status to delivered,
# add distance totals after each delivery, and then back to hub
print(truck1.packages)

def deliver(truck, packages): #Parameters are truck object and package hashmap
    for i in truck.packages:
        p = packages.lookup(i)
        p.update_status("In Transit")

    current_address = "4001 South 700 East"
    total_dist = 0
    while len(truck.packages) > 0:
        dest_address = nearest_neighbor(current_address, truck.packages, distances_list, addresses)
        current_travel_dist = get_distance(get_address_index(current_address, addresses), get_address_index(dest_address, addresses), distances_list)
        total_dist += current_travel_dist
        for i in truck.packages:
            p = packages.lookup(i)
            if p.get_delivery_address() == dest_address:
                p.update_status("Delivered")
                #Need to update time
                truck.packages.remove(i)

        #retrieve packages that have dest_address, change status of packages to delivered in package object, remove all IDs from truck array

    return_home_dist = get_distance(get_address_index(current_address, addresses), get_address_index("4001 South 700 East", addresses), distances_list)
    total_dist += return_home_dist

t = datetime.time(8,0,0)
print(t)
