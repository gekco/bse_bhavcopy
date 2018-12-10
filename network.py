import csv
from datetime import date
from io import BytesIO

import logging

from config import BHAVCOPY_URL
import requests
from zipfile import ZipFile

class Downloader(object):
    '''
    Downloader Class -> To Download Extract and Parse Bhavcopy from URL.
    '''

    def __init__(self, file_date=None):
        if file_date is None:
            file_date = date.today()
        self.url = BHAVCOPY_URL + self._get_file_name(file_date)
        self.serialized_file = None

    def _get_file_name(self, file_date):
        return file_date.strftime("EQ%d%m%y_CSV.ZIP")

    def _download(self):
        print("FETCHING FILE FROM URL : {0}".format(self.url))
        response = requests.get(self.url)
        self.file = BytesIO(response.content)

    def _extract(self):
        try:
            with ZipFile(self.file) as zip:
                self.file = zip.open(zip.filelist[0], mode='r')
        except Exception as e:
            raise Exception("Error Occured while Downloading and Extracting File. Please Make Sure The URL is Correct ({0})".format(e))

    def _parse(self):
        self.file = [row.decode("utf-8") for row in self.file]
        return [{k: v for k, v in row.items()} for row in csv.DictReader(self.file)]

    def serialize(self):
        self._download()
        self._extract()
        return self._parse()

