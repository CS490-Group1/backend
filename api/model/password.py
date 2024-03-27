import bcrypt
class Password:
    def __init__(self, email, password, salt=bcrypt.gensalt()):
        self.email = email,
        self.salt = salt
        self.password = self.hash_password(password)
        

    def hash_password(self, password):
        bytes = password.encode('utf-8')
        return str(bcrypt.hashpw(bytes, self.salt))