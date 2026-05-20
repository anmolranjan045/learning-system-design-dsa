from user import User
from rate_limiter import RateLimiter

class SlidingWindow(RateLimiter):
    def allowRequest(self, UserId) -> bool:
        print('Inside SlidingWindow Allow Request')
