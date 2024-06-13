class Friend:
    def __init__(self, friendID, name, email):
        self.friendID = friendID
        self.name = name
        self.email = email

    def registerFriend(self, user):
        user.friends.append(self)

    @staticmethod
    def checkFriendInfo(user):
        return user.friends
