from user_tier import UserTier
from rate_limiter_config import RateLimiterConfig
from rate_limit_type import RateLimiterType
from rate_limiter_factory import RateLimiterFactory
from user import User

class RateLimiterService:
    def __init__(self):
        self.rateLimiters = {
            UserTier.FREE: RateLimiterFactory.get_limiter(
                RateLimiterType.FixedWindow, RateLimiterConfig(5, 60)),
            UserTier.PREMIUM: RateLimiterFactory.get_limiter(
                RateLimiterType.TokenBucket, RateLimiterConfig(10, 60))
        }
    
    def allowRequest(self, user: User) -> bool:
        limiter = self.rateLimiters[user.tier]
        return limiter.allowRequest(user.userId)