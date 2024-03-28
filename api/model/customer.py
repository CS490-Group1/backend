from api.model.password import Password

class Customer:
    def __init__(self, email=None, first_name=None, last_name=None, dob=None, drivers_license=None, phone=None, password=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.drivers_license = drivers_license
        self.phone = phone
        self.password = Password(self.email, password) if password is not None else None