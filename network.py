import csv
from io import FileIO, StringIO, BytesIO

import logging

from config import BHAVCOPY_URL
import requests
from zipfile import ZipFile

class Downloader(object):
    '''
    Downloader Class -> To Download Extract and Parse Bhavcopy from URL.
    '''

    def __init__(self):
        self.url = BHAVCOPY_URL
        self.serialized_file = None

    def _download(self):
        response = requests.get(self.url)
        self.file = BytesIO(response.content)

    def _extract(self):
        with ZipFile(self.file) as zip:
            try:
                self.file = zip.open(zip.filelist[0], mode='r')
            except Exception as e:
                raise Exception("Error Occured while Downloading and Extracting File.({0})".format(e))

    def _parse(self):
        self.file = [row.decode("utf-8") for row in self.file]
        return [{k: v for k, v in row.items()} for row in csv.DictReader(self.file)]

    def serialize(self):
        self._download()
        self._extract()
        return self._parse()

