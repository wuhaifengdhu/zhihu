import redis
import pickle


pool = redis.ConnectionPool(host='wudevin.com', port=6379)


class RedisHelper(object):
    def __init__(self):
        self.redis = redis.Redis(connection_pool=pool)

    def save(self, user):
        self.redis.set(user.get_user_id(), pickle.dumps(user))

    def get(self, user_id):
        user = self.redis.get(user_id)
        return pickle.loads(user)


if __name__ == '__main__':
    pass
