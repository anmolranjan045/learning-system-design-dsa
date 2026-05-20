class RateLimiterConfig:
    def __init__(self, requests: int, window: int):
        self.requests = requests
        self.window = window