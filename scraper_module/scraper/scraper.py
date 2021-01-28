from bs4 import BeautifulSoup
import requests

SOLD_OUT_CONFIRMATION = "confirmed sold out"
AVAILABLE_CONFIRMATION = "confirmed available"
SOMETHING_WENT_WRONG = "something went wrong"

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = "https://www.flipkart.com/asus-vivobook-14-ryzen-7-octa-core-4700u-8-gb-512-gb-ssd-windows-10-home-m413ia-ek586t-thin-light-laptop/p/itm9bde1d5a8a463?pid=COMFSKF97GXJKYCP&lid=LSTCOMFSKF97GXJKYCPIF0NRS&marketplace=FLIPKART"

def get_requests():
    response = requests.get(url=url, headers=headers)
    return response.text

def get_stock_status():
    soup = BeautifulSoup(get_requests(), "html.parser")
    try:
        common_div = soup.select('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-5-12._78xt5Y > div:nth-child(2)')
        sold_out = common_div[0].select_one('div > button')
        if sold_out:
            return SOLD_OUT_CONFIRMATION

        available = common_div[0].select('div > ul > li:nth-child(2) > form > button')
        if available:
            return AVAILABLE_CONFIRMATION

        return SOMETHING_WENT_WRONG
    except:
        return SOMETHING_WENT_WRONG