class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password


user = UserAccount('admin@bk.ru', 'Admin', '12345')
print(user.check_password('123'))
user.set_password('123')
print(user.check_password('123'))
