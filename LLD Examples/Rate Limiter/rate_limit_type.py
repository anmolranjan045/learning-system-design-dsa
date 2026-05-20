from enum import Enum

class RateLimiterType(Enum):
    FixedWindow = 'FIXEDWINDOW'
    SlidingWindow = 'SLIDINGWINDOW'
    TokenBucket = 'TOKENBUCKET'