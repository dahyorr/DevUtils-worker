import redis
from settings import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

RedisClient = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD
)
