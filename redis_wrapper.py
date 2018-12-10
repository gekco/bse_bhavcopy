from redis import Redis

from config import FIELDS, PRIMARY_KEY, REDIS_URL


class RedisWrapper(object):

    def __init__(self):
        self.connection = Redis.from_url(url=REDIS_URL)
        self._fields = FIELDS
        self.primary_key = PRIMARY_KEY

    def flush_redis(self):
        self.connection.flushall()

    def save_csv(self, rows ):
        self.flush_redis()
        for row in rows:
            pk = row[self.primary_key]
            for key,value in row.items():
                value = value.strip()
                if key in self._fields:
                    self.connection.hset(pk, key, value)

    def _decode_dict(self, encoded_dict):
        return {key.decode("utf-8") : value.decode("utf-8") for key,value in encoded_dict.items()}


    def filter(self, pk_saerchstr, page_number, page_size ):
        pk_saerchstr = pk_saerchstr.upper()

        # Get the Results from Redis
        results = self.connection.keys("*" + pk_saerchstr +"*")

        # Sort The Results
        results = sorted(results, key = lambda x: x.decode("utf-8").startswith(pk_saerchstr), reverse=True )

        # Paginate The Results
        start_index = min((page_number-1)*page_size, len(results))
        end_index = min(page_number*page_size, len(results))


        filtered = []
        for i in range(start_index,end_index):
            filtered.append(self._decode_dict(self.connection.hgetall(results[i])))

        return filtered