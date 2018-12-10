1. Python Script To Download The Days Bhavcopy Zip , extract parse and save into Redis

      python main.py (optional)<date dd-mm-yy>

      by default it will fetch todays bhavcopy

2. To run the server
      python3 -m venv new_venv
      source ./new_env/bin/activate
      pip install -r requirements.txt
      set up the config
      python server.py

3. Config
   1. URL of the bhavcopy file
         BHAVCOPY_URL = "https://www.bseindia.com/download/BhavCopy/Equity/"
   2. Fields which you want to save:
        FIELDS = ["SC_NAME", "SC_CODE", "OPEN", "HIGH", "LOW", "CLOSE"]
   3. PRIMARY_KEY Fields with which you can search the records saved by the script
        PRIMARY_KEY = ["SC_NAME" , "SC_CODE"]
   4. Redis URL
       REDIS_URL= os.environ.get('REDIS_URL', "redis://localhost:6379")
   5. Date Format for the Python Script
      DATE_FORMAT = "%d-%m-%y"
