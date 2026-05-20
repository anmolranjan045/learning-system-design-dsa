from rate_limit_type import RateLimiterType
from fixed_window import FixedWindow
from token_bucket import TokenBucket
from rate_limiter_config import RateLimiterConfig
from rate_limiter import RateLimiter

class RateLimiterFactory:
    @staticmethod
    def get_limiter(type_: RateLimiterType, config: RateLimiterConfig) -> RateLimiter:
        if type_ == RateLimiterType.FixedWindow:
            return FixedWindow(config, type_)
        elif type_ == RateLimiterType.TokenBucket:
            return TokenBucket(config, type_)
        # Add SlidingWindow etc.
        raise ValueError("Unknown Limiter Type")