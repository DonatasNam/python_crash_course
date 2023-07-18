class User:
    def __init__(self, first_name, last_name, age, gender) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
        pass
    
    def decribe_user(self):
        print(f'Users name and surname: {self.first_name} {self.last_name}')
        print(f'Users age: {self.age}')
        print(f'Users gender: {self.gender}')

    def increment_login_attempts(self,attempts):
        self.login_attempts += attempts
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Matt", "Jacobs", "34", "Man")

user1.decribe_user()

for i in range(3):
    user1.increment_login_attempts(10)

print(user1.login_attempts)

user1.reset_login_attempts()

print(user1.login_attempts)