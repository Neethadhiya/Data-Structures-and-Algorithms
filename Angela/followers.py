class User:
    def __init__(self,user_id,user_name):
        self.user_id=user_id
        self.user_name=user_name
    def follow(self,user):
        user.followers+=1
        user.following+=1