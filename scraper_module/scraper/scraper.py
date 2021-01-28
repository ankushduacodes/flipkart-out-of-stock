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

url = "https://www.flipkart.com/samsung-galaxy-j6-black-64-gb/p/itmf5bkh5snxdanh?pid=MOBF5BKHAK33A75F&lid=LSTMOBF5BKHAK33A75F9BQD76&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=4a7ca13b-bb65-4dfd-a4e8-71334dea0c9a.MOBF5BKHAK33A75F.SEARCH&ppt=sp&ppn=sp&ssid=vkc51wtjog0000001611762381384&qH=66edc8224a054df1"

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