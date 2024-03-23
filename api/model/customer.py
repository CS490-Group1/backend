class Customer:
    def __init__(self, email, first_name, last_name, dob, drivers_license, phone, password):
        self.cust_id=None
        self.role="customer"
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.drivers_license = drivers_license
        self.phone = phone
        self.password = password