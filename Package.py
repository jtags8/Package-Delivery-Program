class Package:

    def __init__(self, package_id, delivery_address, city, state, zipcode, deadline, weight, status):
        self.package_id = package_id
        self.delivery_address = delivery_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.delivery_time = None

    def update_status(self, status):
        self.status = status

    def update_delivery_time(self, time):
        self.delivery_time = time

    def update_delivery_address(self, address):
        self.delivery_address = address

    def get_package_id_from_add(self, address):
        if address == self.delivery_address:
            return self.package_id
        return None

    def get_delivery_address(self):
        return self.delivery_address

    def __str__(self) -> str:
        return (f'Package {self.package_id}: Delivery address: {self.delivery_address}, {self.city}, {self.state} {self.zipcode}, '
                f'Deadline: {self.deadline}, Weight in kg: {self.weight}, Delivery status: {self.status}')