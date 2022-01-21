import redis
from settings import REDIS_HOST, REDIS_PORT

RedisClient = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT
)
