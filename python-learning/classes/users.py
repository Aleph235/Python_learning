class Users:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0
   
    def describe_user(self):
        print(f"User informations:\n-{self.first_name.title()}\n-{self.last_name.title()}\n-{self.age}\n-{self.sex}")
    
    def greet_user(self):
        if self.sex == 'male':
            print(f"Hello mister {self.last_name.title()}")
        else:
            print(f"Hello madame {self.last_name.title()}")

    def increment_login_attempts(self,login_attempts):
        self.login_attempts += 1

    def reset_login_attempts(self,login_attempts):
        self.login_attempts = 0


user1 = Users('jalal','alhamadany',44,'male')
user2 = Users('francesca','dipietro',19,'female')

user1.increment_login_attempts(user1.login_attempts)
user1.increment_login_attempts(user1.login_attempts)
user1.increment_login_attempts(user1.login_attempts)
user1.increment_login_attempts(user1.login_attempts)
user1.increment_login_attempts(user1.login_attempts)
print(f"{user1.login_attempts}")

user1.reset_login_attempts(user1.login_attempts)
print(f"{user1.login_attempts}")

user1.describe_user()
user1.greet_user()

user2.greet_user()
