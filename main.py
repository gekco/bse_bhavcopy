import sys
from datetime import date, datetime

from config import BHAVCOPY_URL, DATE_FORMAT
from network import Downloader
from redis_wrapper import RedisWrapper


class Manager(object):
    '''
    Manager Class - > Wrapper for the server/user to save or fetch data from redis
    '''
    def __init__(self, file_date=None):
        self.redis = RedisWrapper()
        self.downloader = Downloader(file_date)

    def download_and_save_bhavcopy(self):
        native_data = self.downloader.serialize()
        self.redis.save_csv(native_data)

    def filter_results(self, searchstr, page_size, page_number):
        return self.redis.filter(searchstr,page_number= page_number, page_size=page_size)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_date = datetime.strptime(sys.argv[1], DATE_FORMAT)
    else:
        file_date = datetime.today()
    manager = Manager(file_date)
    manager.download_and_save_bhavcopy()
    print("SUCCESS :)")


