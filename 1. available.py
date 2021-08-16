import requests
import urllib3
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Process, Manager
from colorama import init, Fore
import multiprocessing 
from time import sleep

init(autoreset=True)
urllib3.disable_warnings()

def golant(number):
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
    # The loop is to make sure the request has no errors so the code wont stop in the middle
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
    # 60 threads to make it faster
    p = multiprocessing.Pool(60)
    with open('golant.txt', 'w') as f:
        # Golan only allow numbers from 058-5000000 to 058-7999999
        for result in p.imap(golant, range(500000,7999999+1)):
            print(result)
            # un for unavailable
            if "un" not in result:
                f.write(result + '\n')

if __name__=='__main__':
    mp_handler()