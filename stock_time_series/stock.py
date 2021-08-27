'''
@Author: Naziya
@Date: 2021-08-26
@Last Modified by: Naziya
@Last Modified : 2021-08-26
@Title : Program Aim is to get the live stock data from the url.
'''

from dotenv import load_dotenv
load_dotenv()
from LoggerFormat import logger
import os
import csv
import requests

try:
    demo = os.getenv("API_KEY")

    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=1min&slice=year1month1&apikey={}'.format(demo)

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            print(row)
except Exception as err:
    logger.error(err)
    
