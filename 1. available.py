import requests
import urllib3
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Process, Manager
from colorama import init, Fore
import multiprocessing 
from time import sleep

init(autoreset=True)
urllib3.disable_warnings()

def partner():
    headers = {
    'Host': 'my.partner.co.il',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Brand': 'orange',
    'Category': 'plans',
    'Platform': 'WEB',
    'Subcategory': 'plans',
    'Appname': 'plans',
    'Useruniqueid': '10202119465948fd2b9d-5c9c-8933-3337-8115200adb75',
    'Content-Type': 'application/json',
    'Content-Length': '22',
    'Origin': 'https://www.partner.co.il',
    'Referer': 'https://www.partner.co.il/',
    'Te': 'trailers',
    'Connection': 'close',
    }

    data = '{\\"isKosherPlan\\":false}'

    response = requests.post('https://my.partner.co.il/PlansApi/Plans/GetListNewMsisdnNumber', headers=headers, data=data, verify=False)

def we4g(number):
    cookies = {
    'ea665a87302479a2702d938bca74ec90': '2rbp9ntp3t8hhqcng5b3ihlqsm',
    'visid_incap_1504225': 'ol06SmbASzueKZlRRYDAen3/6WAAAAAAQUIPAAAAAACZQAX9Thf/ENvxta2v/5Zt',
    'incap_ses_253_1504225': 'ya+GOO7ZE1TROGRoXtaCA37/6WAAAAAAkTtGcv3Oi9vprcaOIqabiw==',
    'usfu_lzdmENwEGM3fqlb6KbVsrw%3d%3d': 'true',
    '_gcl_au': '1.1.44664793.1625948032',
    'poptin_old_user': 'true',
    'poptin_user_id': '0.u1fm43go9n',
    '_ga': 'GA1.3.645039358.1625948033',
    '_gid': 'GA1.3.487682881.1625948033',
    'poptin_referrer': 'https://www.google.com/',
    'poptin_user_ip': '213.8.115.137',
    'poptin_user_country_code': 'false',
    'poptin_o_v_25634b03978e5': '997e1106f98f8',
    'poptin_session_account_cd9f463c6a075': 'true',
    'poptin_session': 'true',
    'poptin_c_visitor': 'true',
    '_fbp': 'fb.2.1625948035601.129305736',
    'poptin_o_a_d_25634b03978e5': '997e1106f98f8',
    'poptin_c_p_o_x_c_25634b03978e5': '25634b03978e5',
    }

    headers = {
        'Host': 'www.we4g.co.il',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '111',
        'Origin': 'https://www.we4g.co.il',
        'Referer': 'https://www.we4g.co.il/he/',
        'Te': 'trailers',
        'Connection': 'close',
    }

    params = (
        ('option', 'com_we'),
        ('task', 'sale.checkNewNumberAvailability'),
        ('format', 'raw'),
    )
    num = "{:07}".format(number)
    data = f'number=051{num}&weSecurityToken=2ae7dfee791eadeb6c524c2f5cd5a4ba&googleAnalyticsClientId=645039358.1625948033'
    result = None
    while result is None:
        try:
            response = requests.post('https://www.we4g.co.il/index.php', headers=headers, params=params, cookies=cookies, data=data, verify=False)
            result = 1
        except:
            pass
    d = response.json()
    try:
        a = d['data']["available"]
    except:
        print(Fore.YELLOW + f"ERROR: {response.text}")
    numberr = d['data']["number"] #051XYYYYYY
    
    if d['data']["available"] is True:
        return f"{numberr}"
    elif d['data']["available"] is False:
        return f"{numberr} un"

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
    #Golant
    """
    for i in [7]:
        number = '613371'
        p = multiprocessing.Pool(60)
        with open('temp2.txt', 'w') as f:
            for result in p.imap(golant, range(7613371,7999999+1)):
                print(result)
                if "un" not in result:
                    f.write(result + '\n')
    """
    #Partner
    """
    do:
        p = multiprocessing.Pool(60)
        with open('temp2.txt', 'w') as f:
            for result in p.imap(golant, range(7613371,7999999+1)):
                print(result)
                if "un" not in result:
                    f.write(result + '\n')
    while()
    """
    #We4G
    for i in [2,5]:
        number = '000000'
        p = multiprocessing.Pool(60)
        with open('we4g2.txt', 'w') as f:
            for result in p.imap(we4g, range(2616746,2999999+1)):
                print(result)
                if "un" not in result:
                    f.write(result + '\n')
            for result in p.imap(we4g, range(5000000,5999999+1)):
                print(result)
                if "un" not in result:
                    f.write(result + '\n')

if __name__=='__main__':
    mp_handler()