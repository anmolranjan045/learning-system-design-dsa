from user import User
from user_tier import UserTier
from rate_limiter_service import RateLimiterService
import time

rateLimiterService = RateLimiterService()

freeUser = User('123', UserTier.FREE)
preminumUser = User('999', UserTier.PREMIUM)

for i in range(10):
    allowed: bool = rateLimiterService.allowRequest(freeUser)
    print(f"Request {i + 1} for Free User is Allowed: {allowed}")
    time.sleep(2)

for i in range(10):
    allowed: bool = rateLimiterService.allowRequest(preminumUser)
    print(f"Request {i + 1} for Premium User is Allowed: {allowed}")
    time.sleep(2)