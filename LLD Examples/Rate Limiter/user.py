from user_tier import UserTier

class User:
    def __init__(self, userId: str, tier: UserTier):
        self.userId = userId
        self.tier = tier
        
    def getuser(self) -> UserTier:
        return self.tier
    
    def getUserId(self) -> str:
        return self.userId