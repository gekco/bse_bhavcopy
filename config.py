import os

BHAVCOPY_URL = "https://www.bseindia.com/download/BhavCopy/Equity/EQ071218_CSV.ZIP"
REDIS_HOST = "h:p6c895f432028518e1b3e0353573717d3906b4b41afc747a083579e6ea92c9919@ec2-54-209-190-123.compute-1.amazonaws.com"
REDIS_PORT = 45859
REDIS_DB = 0
FIELDS = ["SC_NAME", "SC_CODE", "OPEN", "HIGH", "LOW", "CLOSE"]
PRIMARY_KEY = "SC_NAME"
REDIS_URL= os.environ.get('REDIS_URL', "")
