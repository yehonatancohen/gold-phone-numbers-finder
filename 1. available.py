import requests
import urllib3
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Process, Manager
from colorama import init, Fore
import multiprocessing 
from time import sleep

init(autoreset=True)
urllib3.disable_warnings()

def check(number):
    headers = {
    'Host': 'myaccount.golantelecom.co.il',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Access-Control-Request-Method': 'GET',
    'Access-Control-Request-Headers': 'platform-name',
    'Referer': 'https://www.golantelecom.co.il/',
    'Origin': 'https://www.golantelecom.co.il',
    'Te': 'trailers',
    'Connection': 'close',
    }
    num = "{:07}".format(number)
    result = None
    while result is None:
        try:
            response = requests.get(f'https://myaccount.golantelecom.co.il/rpc/registration/msisdn/isavailable?ndc_sn=58{num}',headers=headers, verify=False)
            result = 1
        except:
            pass
    d = response.json()
    try:
        a = d['data']["is_available"]
    except:
        print(Fore.YELLOW + f"ERROR: {response.text}")

    numberr = d['data']["ndc_sn"] #58XYYYYYY
    
    if d['data']["is_available"] is True:
        return f"0{numberr}"
    elif d['data']["is_available"] is False:
        return f"0{numberr} un"

def mp_handler():
    for i in [7]:
        number = '613371'
        p = multiprocessing.Pool(60)
        with open('temp2.txt', 'w') as f:
            for result in p.imap(check, range(7613371,7999999+1)):
                print(result)
                if "un" not in result:
                    f.write(result + '\n')

if __name__=='__main__':
    mp_handler()