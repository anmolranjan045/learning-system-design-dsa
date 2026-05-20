from rate_limiter import RateLimiter
import time

class TokenBucket(RateLimiter):
    def __init__(self, config, type_):
        super().__init__(config, type_)
        self.state = {} # {user_id: [tokens, last_refill_time]}

    def allowRequest(self, userId: str) -> bool:
        now = time.time()
        if userId not in self.state:
            self.state[userId] = [self.rateLimiterConfig.requests, now]
            
        tokens, last_refill = self.state[userId]
        
        # Refill logic
        elapsed = now - last_refill
        new_tokens = elapsed * (self.rateLimiterConfig.requests / self.rateLimiterConfig.window)
        tokens = min(self.rateLimiterConfig.requests, tokens + new_tokens)
        
        if tokens >= 1:
            self.state[userId] = [tokens - 1, now]
            return True
        return False