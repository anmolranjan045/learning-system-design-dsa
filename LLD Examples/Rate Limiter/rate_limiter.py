from rate_limiter_config import RateLimiterConfig
from rate_limit_type import RateLimiterType
from abc import ABC, abstractmethod
from user import User

class RateLimiter(ABC):
    def __init__(self, rateLimiterConfig: RateLimiterConfig, rateLimiterType: RateLimiterType):
        self.rateLimiterConfig = rateLimiterConfig
        self.rateLimiterType = rateLimiterType
    
    @abstractmethod
    def allowRequest(self, UserId: User) -> bool:
        pass