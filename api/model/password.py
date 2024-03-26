class Password:
    def __init__(self, email, password):
        self.email = email,
        self.password = hash(password)