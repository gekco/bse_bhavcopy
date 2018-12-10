import os

BHAVCOPY_URL = "https://www.bseindia.com/download/BhavCopy/Equity/EQ071218_CSV.ZIP"
FIELDS = ["SC_NAME", "SC_CODE", "OPEN", "HIGH", "LOW", "CLOSE"]
PRIMARY_KEY = "SC_NAME"
REDIS_URL= os.environ.get('REDIS_URL', "redis://localhost:6379")
