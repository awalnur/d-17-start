class User:
    def __init__(self, id, name):
        self.user_id = id
        self.name = name
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.following += 1
        self.followers += 1

user_1 = User('001', 'awalnur')
user_2 = User('002', 'awal')
user_1.follow(user_2)

print(user_1.followers)