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

def nearest_neighbor(current_address, truck_packages, package_hash_list, distances, address_list):

    min_distance = float('inf')
    nearest_address_index = 0
    current_address_index = get_address_index(current_address, address_list)

    for i in truck_packages:
        p = package_hash_list.lookup(str(i))
        target_address_index = get_address_index(p.get_delivery_address(), address_list)
        distance = get_distance(current_address_index, target_address_index, distances)
        if float(distance) == 0:
            continue

        if float(distance) < float(min_distance):
            min_distance = distance
            nearest_address_index = target_address_index - 1
    nearest_address = address_list[nearest_address_index]

    return nearest_address

distances_list = load_data('distances.csv')
addresses_for_distances_list = load_data('addresses_for_distances.csv')
addresses = []
for a in addresses_for_distances_list:
    addresses.append(a[0])

new_package_list = load_data('Packages.csv')
package_hashmap = HashMap()

for row in new_package_list:
    package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], "At the hub")
    package_hashmap.insert(row[0], package)
    #print(str(package_hashmap.lookup(row[0])))

truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

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
truck2.load(2)
truck2.load(3)
truck2.load(5)
truck2.load(7)
truck2.load(8)
truck2.load(10)
truck2.load(18)
truck2.load(22)
truck2.load(24)
truck2.load(29)
truck2.load(30)
truck2.load(33)
truck2.load(36)
truck2.load(37)
truck2.load(38)
truck3.load(6)
truck3.load((package_hashmap.get_hash(9)
truck3.load((package_hashmap.get_hash(11)
truck3.load((package_hashmap.get_hash(12)
truck3.load((package_hashmap.get_hash(21)
truck3.load((package_hashmap.get_hash(23)
truck3.load((package_hashmap.get_hash(25)
truck3.load((package_hashmap.get_hash(26)
truck3.load((package_hashmap.get_hash(27)
truck3.load((package_hashmap.get_hash(28)
truck3.load((package_hashmap.get_hash(31)
truck3.load((package_hashmap.get_hash(32)
truck3.load((package_hashmap.get_hash(35)
truck3.load(39)
truck3.load(40)

def reset_truck(truck, packages): #Parameters are truck object and package hashmap
    for i in truck.packages:
        p = packages.lookup(i)
        p.update_status("At the hub")
def calc_travel_time(distance): #18 mph, can use for individual deliveries or total time
    time_in_seconds = (distance / 18) * 3600
    time = datetime.timedelta(seconds=time_in_seconds)
    return time

def deliver(truck, packages, time_hr, time_min, time_sec): #Parameters are truck object and package hashmap and time to depart, returns total distance traveled
    time_in_seconds = (time_hr * 3600) + (time_min * 60) + time_sec
    time = datetime.timedelta(seconds=time_in_seconds)
    for i in truck.packages:
        p = packages.lookup(str(i))
        p.update_status("In Transit")

    current_address = "4001 South 700 East"
    total_dist = 0
    while len(truck.packages) > 0:
        dest_address = nearest_neighbor(current_address, truck.packages, packages, distances_list, addresses)
        current_travel_dist = float(get_distance(get_address_index(current_address, addresses), get_address_index(dest_address, addresses), distances_list))
        total_dist += current_travel_dist
        for i in truck.packages:
            p = packages.lookup(str(i))
            if p.get_delivery_address() == dest_address:
                travel_time = calc_travel_time(total_dist)
                delivery_time = time + travel_time
                p.update_status("Delivered at " + str(delivery_time))
                p.update_delivery_time(delivery_time)
                truck.packages.remove(i)
        print("Delivery time!")
        for j in range(1, 40):
            print(packages.lookup(str(j)))

    return_home_dist = float(get_distance(get_address_index(current_address, addresses), get_address_index("4001 South 700 East", addresses), distances_list))
    total_dist += return_home_dist

    return total_dist

def start():
    print("Welcome to WGUPS Service! Please choose one of the following options:")
    print("")
    if input

    while True:

# print(truck1.packages)
# p = package_hashmap.lookup(str("1"))
# print(p)
# current_address_index = get_address_index("4001 South 700 East", addresses)
# print(current_address_index)
# target_address_i = get_address_index(p.get_delivery_address(), addresses)
# print(target_address_i)
# distance = get_distance(current_address_index, target_address_i, distances_list)
# print(distance)
# nearest_address_index = target_address_i - 1
# print(nearest_address_index)
# nearest_address = addresses[nearest_address_index]
# print(nearest_address)
# dest_address = nearest_neighbor("4001 South 700 East", truck1.packages, package_hashmap, distances_list, addresses)
# print(dest_address)
truck1_delivery_distance = deliver(truck1, package_hashmap, 8, 0, 0)
print(truck1_delivery_distance)
print(calc_travel_time(truck1_delivery_distance))