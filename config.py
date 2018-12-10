import os

BHAVCOPY_URL = "https://www.bseindia.com/download/BhavCopy/Equity/"
FIELDS = ["SC_NAME", "SC_CODE", "OPEN", "HIGH", "LOW", "CLOSE"]
PRIMARY_KEY = ["SC_NAME" , "SC_CODE"]
REDIS_URL= os.environ.get('REDIS_URL', "redis://localhost:6379")
DATE_FORMAT = "%d-%m-%y"
