from user import User
from rate_limiter import RateLimiter
import time

class FixedWindow(RateLimiter):
    def __init__(self, config, type_):
        super().__init__(config, type_)
        self.state = {}

    def allowRequest(self, userId: str) -> bool:
        now = time.time()
        if userId not in self.state:
            self.state[userId] = [0, now]
            
        count, window_start = self.state[userId]
        
        if now - window_start > self.rateLimiterConfig.window:
            count = 0
            window_start = now
            
        if count < self.rateLimiterConfig.requests:
            self.state[userId] = [count + 1, window_start]
            return True
        return False