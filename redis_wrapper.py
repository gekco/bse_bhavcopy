from redis import Redis

from config import FIELDS, PRIMARY_KEY, REDIS_URL


class RedisWrapper(object):

    def __init__(self):
        self.connection = Redis.from_url(url=REDIS_URL)
        self._fields = FIELDS
        self.primary_keys = PRIMARY_KEY

    def flush_redis(self):
        self.connection.flushall()

    def _generate_pk(self, row, pks):
        '''
        Generate The key corresponding to which the csv row will be saved.
        NOTE : ALL THE FIELDS IN THE PRIMARY KEY CAN BE USED TO SEARCH THE RECORDS
        :param row: row that needs to be saved
        :param pks: list of primary key
        :return: the key
        '''
        return "_".join([row[pk] for pk in pks ])

    def save_csv(self, rows ):
        '''
        SAVE THE CSV IN REDIS
        :param rows: list of records
        :return:
        '''
        self.flush_redis()
        for row in rows:
            pk = self._generate_pk( row, self.primary_keys)
            for key,value in row.items():
                value = value.strip()
                if key in self._fields:
                    self.connection.hset(pk, key, value)

    def _decode_dict(self, encoded_dict):
        '''
        Decode the dicts to utf-8
        :param encoded_dict:
        :return:
        '''
        return {key.decode("utf-8") : value.decode("utf-8") for key,value in encoded_dict.items()}


    def filter(self, pk_saerchstr, page_number, page_size ):
        '''
        Filter the records
        :param pk_saerchstr: Primary Key Saerch String
        :param page_number:
        :param page_size:
        :return: list of filtered records
        '''
        pk_saerchstr = pk_saerchstr.upper()

        # Get the Results from Redis ( All the records that contain the search string )
        results = self.connection.keys("*" + pk_saerchstr +"*")

        # Sort The Results( Put the records that starts with the search string first )
        # results = sorted(results, key = lambda x: x.decode("utf-8").startswith(pk_saerchstr), reverse=True )

        # Paginate The Results
        start_index = min((page_number-1)*page_size, len(results))
        end_index = min(page_number*page_size, len(results))


        filtered = []
        for i in range(start_index,end_index):
            filtered.append(self._decode_dict(self.connection.hgetall(results[i])))

        return filtered