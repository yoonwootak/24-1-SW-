class User:
    def __init__(self, userID, password, name, email):
        self.userID = userID
        self.password = password
        self.name = name
        self.email = email
        self.friends = []

    def login(self, userID, password):
        if self.userID == userID and self.password == password:
            return True
        return False

    def logout(self):
        return True

    @staticmethod
    def signUp(userID, password, name, email):
        return User(userID, password, name, email)

    def registerFriend(self, friend):
        self.friends.append(friend)

    def checkFriendInfo(self):
        return self.friends
