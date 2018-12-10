from config import BHAVCOPY_URL
from network import Downloader
from redis_wrapper import RedisWrapper


class Manager(object):
    def __init__(self):
        self.redis = RedisWrapper()
        self.downloader = Downloader()

    def download_and_save_bhavcopy(self):
        native_data = self.downloader.serialize()
        self.redis.save_csv(native_data)

    def filter_results(self, searchstr, page_size, page_number):
        return self.redis.filter(searchstr,page_number= page_number, page_size=page_size)


if __name__ == "__main__":
    manager = Manager()
    manager.download_and_save_bhavcopy()


