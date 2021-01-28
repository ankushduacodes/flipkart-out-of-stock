from flask import Flask
import time

from scraper_module.email import email_handler
from scraper_module.scraper import scraper

app=Flask(__name__)

@app.route('/')
def home():
    email_sent = False
    while(not email_sent):
        stock_status = scraper.get_stock_status()
        print(stock_status)
        if stock_status == scraper.AVAILABLE_CONFIRMATION:
            email_handler.send_email("Product is now available")
            email_sent = True
        elif stock_status == scraper.SOLD_OUT_CONFIRMATION:
            time.sleep(1800)
        elif stock_status == scraper.SOMETHING_WENT_WRONG:
            email_handler.send_email('Something went wrong, Please check for code logic')
            email_sent = True
    return 'hi'


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=9000, debug=True)